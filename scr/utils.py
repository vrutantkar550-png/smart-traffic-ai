import cv2

def get_video_capture(path):
    return cv2.VideoCapture(path)

def display_frame(frame):
    cv2.imshow("Traffic Feed", frame)

def exit_key():
    return cv2.waitKey(1) & 0xFF == ord('q')
