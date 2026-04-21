import cv2

# Simple vehicle detection using Haar Cascade (basic demo)
car_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'cars.xml')

def detect_vehicles(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cars = car_cascade.detectMultiScale(gray, 1.1, 3)

    vehicle_count = len(cars)

    for (x, y, w, h) in cars:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)

    return vehicle_count, frame
