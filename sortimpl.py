# import os
# os.environ["QT_QPA_PLATFORM"] = "xcb"
import cv2
import numpy as np

# Minimal SORT implementation (for demo, not full feature)
class Sort:
    def __init__(self):
        self.next_id = 0
        self.tracks = {}

    def update(self, detections):
        # detections: list of [x1, y1, x2, y2]
        # For simplicity, assign new IDs every frame (no real tracking here)
        tracked_objects = []
        for det in detections:
            tracked_objects.append(det.tolist() + [self.next_id])
            self.next_id += 1
        return tracked_objects

def get_centroid(box):
    x1, y1, x2, y2 = box
    cx = int((x1 + x2) / 2)
    cy = int((y1 + y2) / 2)
    return cx, cy

# Video source
cap = cv2.VideoCapture('people-entering-shopping-mall-slowed.mp4')  # Replace with your video path or 0 for webcam

# Background subtractor
fgbg = cv2.createBackgroundSubtractorMOG2(history=500, varThreshold=50)

# Initialize tracker
tracker = Sort()

# Line position (y coordinate)
line_y = 250
# Add this helper function
def get_centroid(bbox):
    x1, y1, x2, y2 = bbox
    return ((x1 + x2) // 2, (y1 + y2) // 2)

# Initialize before main loop
prev_centroids = {}  # Persistent centroid storage
count = 0
offset = 10  # Hysteresis band
tracked_objects_state = {}  # Track crossing state per object

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Processing pipeline (same as before)
    frame = cv2.resize(frame, (640, 480))
    fgmask = fgbg.apply(frame)
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)
    fgmask = cv2.dilate(fgmask, kernel, iterations=2)
    contours, _ = cv2.findContours(fgmask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    detections = []
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 500:
            x, y, w, h = cv2.boundingRect(cnt)
            detections.append([x, y, x + w, y + h])
    
    tracked_objects = tracker.update(np.array(detections))
    cv2.line(frame, (0, line_y), (frame.shape[1], line_y), (0, 0, 255), 2)
    
    current_centroids = {}
    
    for box in tracked_objects:
        x1, y1, x2, y2, obj_id = map(int, box)
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(frame, str(obj_id), (x1, y1 - 10), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)
        
        cx, cy = get_centroid((x1, y1, x2, y2))
        current_centroids[obj_id] = (cx, cy)
        
        # Initialize state for new objects
        if obj_id not in tracked_objects_state:
            tracked_objects_state[obj_id] = {
                'counted': False,
                'last_side': 'above' if cy < line_y else 'below'
            }
        
        # Get current state
        state = tracked_objects_state[obj_id]
        
        # Determine current side with hysteresis
        current_side = None
        if cy < line_y - offset:
            current_side = 'above'
        elif cy > line_y + offset:
            current_side = 'below'
        
        # Count crossings only when object fully crosses the hysteresis band
        if current_side and state['last_side'] and current_side != state['last_side']:
            print(1)
            # Downward crossing
            if state['last_side'] == 'above' and current_side == 'below':
                count += 1
                print(f"ID {obj_id} entered. Count: {count}")
            # Upward crossing
            elif state['last_side'] == 'below' and current_side == 'above':
                count -= 1
                print(f"ID {obj_id} exited. Count: {count}")
            
            # Update state after counting
            state['last_side'] = current_side
    
    # Update previous centroids for next frame
    prev_centroids = current_centroids.copy()
    
    cv2.putText(frame, f"Count: {count}", (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)

    cv2.imshow('Frame', frame)
    cv2.imshow('FG Mask', fgmask)

    key = cv2.waitKey(30)
    if key == 27:  # ESC key to stop
        break

cap.release()
cv2.destroyAllWindows()
