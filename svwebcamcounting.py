import numpy as np
import supervision as sv
from ultralytics import YOLO
import cv2
from datetime import datetime

def main():
    cap = cv2.VideoCapture(0)

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS) or 30

    model = YOLO("models/yolo11n.pt")

    byte_tracker = sv.ByteTrack()
    bounding_box_annotator = sv.BoundingBoxAnnotator(thickness=4)
    label_annotator = sv.LabelAnnotator(text_thickness=4, text_scale=2)
    trace_annotator = sv.TraceAnnotator(thickness=4)
    line_zone_annotator = sv.LineZoneAnnotator(thickness=4, text_thickness=4, text_scale=2)

    # Define a horizontal line somewhere on the screen
    # TODO param specifying line
    # line_y_pos = int(height / 1.5)
    # START = sv.Point(0, line_y_pos)
    # END = sv.Point(width, line_y_pos)
    # line_zone = sv.LineZone(start=START, end=END)
    line_x_pos = int(width / 2)
    START = sv.Point(line_x_pos, 0)
    END = sv.Point(line_x_pos, height)
    line_zone = sv.LineZone(start=START, end=END)
    
    now = datetime.now()
    formatted = now.strftime("%H:%M-%d-%B-%Y")
    sink = sv.VideoSink(target_path=f"results/webcam_output_{formatted.strip()}.mp4", video_info=sv.VideoInfo(width=width, height=height, fps=fps))
    
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Inference and tracking
        results = model(frame, verbose=False)[0]
        detections = sv.Detections.from_ultralytics(results)
        detections = byte_tracker.update_with_detections(detections)

        # Label format: #tracker_id class confidence
        labels = [
            f"#{tracker_id} {model.model.names[class_id]} {confidence:0.2f}"
            for confidence, class_id, tracker_id
            in zip(detections.confidence, detections.class_id, detections.tracker_id)
        ]

        # Annotate frame
        annotated_frame = frame.copy()
        annotated_frame = trace_annotator.annotate(annotated_frame, detections)
        annotated_frame = bounding_box_annotator.annotate(annotated_frame, detections)
        annotated_frame = label_annotator.annotate(annotated_frame, detections, labels)

        # Trigger and draw line zone
        line_zone.trigger(detections)
        annotated_frame = line_zone_annotator.annotate(annotated_frame, line_counter=line_zone)

        # Show frame
        cv2.imshow("Webcam + Supervision", annotated_frame)

        # Save to file
        with sink:
            sink.write_frame(annotated_frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    sink.close()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
