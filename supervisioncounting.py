import numpy as np
import supervision as sv
from ultralytics import YOLO
import cv2

def main():
    SOURCE_VIDEO_PATH = f"videos/scaleddown-FootfallVideo.mp4"

    generator = sv.get_video_frames_generator(SOURCE_VIDEO_PATH)
    frame = next(generator)

    sv.VideoInfo.from_video_path(SOURCE_VIDEO_PATH)

    model = YOLO("models/yolo11n.pt")

    results = model(frame, verbose=False)[0]
    detections = sv.Detections.from_ultralytics(results)

    ##################
    bounding_box_annotator = sv.BoundingBoxAnnotator(thickness=4)
    annotated_frame = bounding_box_annotator.annotate(frame.copy(), detections)

    labels = [
        f"{results.names[class_id]} {confidence:0.2f}"
        for class_id, confidence
        in zip(detections.class_id, detections.confidence)
    ]

    bounding_box_annotator = sv.BoundingBoxAnnotator(thickness=4)
    label_annotator = sv.LabelAnnotator(text_thickness=4, text_scale=2)

    annotated_frame = frame.copy()
    annotated_frame = bounding_box_annotator.annotate(annotated_frame, detections)
    annotated_frame = label_annotator.annotate(annotated_frame, detections, labels)
    ##################
    
    bounding_box_annotator = sv.BoundingBoxAnnotator(thickness=1)
    annotated_frame = bounding_box_annotator.annotate(frame.copy(), detections)

    v = sv.VideoInfo.from_video_path(SOURCE_VIDEO_PATH)

    line_y_pos = int(v.height / 1.5)
    START = sv.Point(0, line_y_pos)
    END = sv.Point(v.width, line_y_pos)
    line_zone = sv.LineZone(start=START, end=END)

    line_zone_annotator = sv.LineZoneAnnotator(
        thickness=4,
        text_thickness=4,
        text_scale=2)

    annotated_frame = frame.copy()
    annotated_frame = line_zone_annotator.annotate(annotated_frame, line_counter=line_zone)

    byte_tracker = sv.ByteTrack()

    bounding_box_annotator = sv.BoundingBoxAnnotator(thickness=4)
    label_annotator = sv.LabelAnnotator(text_thickness=4, text_scale=2)
    trace_annotator = sv.TraceAnnotator(thickness=4)

    def callback(frame: np.ndarray, index:int) -> np.ndarray:
        results = model(frame, verbose=False)[0]
        detections = sv.Detections.from_ultralytics(results)
        detections = byte_tracker.update_with_detections(detections)

        labels = [
            f"#{tracker_id} {model.model.names[class_id]} {confidence:0.2f}"
            for confidence, class_id, tracker_id
            in zip(detections.confidence, detections.class_id, detections.tracker_id)
        ]

        annotated_frame = frame.copy()
        annotated_frame = trace_annotator.annotate(annotated_frame, detections)
        annotated_frame = bounding_box_annotator.annotate(annotated_frame, detections)
        annotated_frame = label_annotator.annotate(annotated_frame, detections, labels)

        line_zone.trigger(detections)

        # Annotate with line counter
        annotated_frame = line_zone_annotator.annotate(annotated_frame, line_counter=line_zone)

        # Show the frame using OpenCV
        cv2.imshow("Video + Supervision", annotated_frame)
        key = cv2.waitKey(1)
        if key == ord('q'):
            raise KeyboardInterrupt("Video display interrupted by user.")

        return annotated_frame

    TARGET_VIDEO_PATH = f"results/supervision-FootfallVideo.mp4"

    sv.process_video(
        source_path = SOURCE_VIDEO_PATH,
        target_path = TARGET_VIDEO_PATH,
        callback=callback
    )

if __name__ == "__main__":
    main()