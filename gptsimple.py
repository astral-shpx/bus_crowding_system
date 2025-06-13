import cv2
import numpy as np

# Minimal SORT-like tracker (not real tracking, just demo)
class Sort:
    def __init__(self):
        self.next_id = 0
        self.tracks = {}

    def update(self, detections):
        tracked_objects = []
        for det in detections:
            tracked_objects.append(det.tolist() + [self.next_id])
            self.next_id += 1
        return tracked_objects

def get_centroid(box):
    x1, y1, x2, y2 = box
    return ((x1 + x2) // 2, (y1 + y2) // 2)

# --- Setup ---
cap = cv2.VideoCapture('walking_people.mp4')  # Replace with your video

fgbg = cv2.createBackgroundSubtractorMOG2(history=500, varThreshold=50)
tracker = Sort()

line_y = 250
offset = 10
count = 0
tracked_objects_state = {}

# --- Main loop ---
while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.resize(frame, (640, 480))

    fgmask = fgbg.apply(frame)
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)
    fgmask = cv2.dilate(fgmask, kernel, iterations=2)

    contours, _ = cv2.findContours(fgmask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    detections = []
    for cnt in contours:
        if cv2.contourArea(cnt) > 500:
            x, y, w, h = cv2.boundingRect(cnt)
            detections.append([x, y, x + w, y + h])
    
    tracked_objects = tracker.update(np.array(detections))

    # Draw line
    cv2.line(frame, (0, line_y), (frame.shape[1], line_y), (0, 0, 255), 2)

    for box in tracked_objects:
        x1, y1, x2, y2, obj_id = map(int, box)
        cx, cy = get_centroid((x1, y1, x2, y2))

        # Draw bounding box and ID
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(frame, str(obj_id), (x1, y1 - 10), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)
        cv2.circle(frame, (cx, cy), 3, (0, 0, 255), -1)

        # Initialize state
        if obj_id not in tracked_objects_state:
            tracked_objects_state[obj_id] = {
                'last_side': 'above' if cy < line_y else 'below'
            }

        state = tracked_objects_state[obj_id]
        last_side = state['last_side']

        # Determine current side with hysteresis
        current_side = None
        if cy < line_y - offset:
            current_side = 'above'
        elif cy > line_y + offset:
            current_side = 'below'

        # Count crossing
        if current_side and current_side != last_side:
            if last_side == 'above' and current_side == 'below':
                count += 1
                print(f"ID {obj_id} entered ↓. Count: {count}")
            elif last_side == 'below' and current_side == 'above':
                count -= 1
                print(f"ID {obj_id} exited ↑. Count: {count}")

            # Update side
            tracked_objects_state[obj_id]['last_side'] = current_side

    # Display count
    cv2.putText(frame, f"Count: {count}", (10, 40), 
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)

    cv2.imshow('Frame', frame)
    cv2.imshow('FG Mask', fgmask)

    if cv2.waitKey(30) & 0xFF == 27:  # ESC to quit
        break

cap.release()
cv2.destroyAllWindows()
