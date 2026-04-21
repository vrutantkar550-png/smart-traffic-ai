from detection import detect_vehicles
from traffic_control import control_signal
from utils import get_video_capture, display_frame, exit_key

video_path = "../data/sample_video.mp4"

cap = get_video_capture(video_path)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    vehicle_count, frame = detect_vehicles(frame)
    signal_time = control_signal(vehicle_count)

    print(f"Vehicles: {vehicle_count}, Green Time: {signal_time}s")

    display_frame(frame)

    if exit_key():
        break

cap.release()
