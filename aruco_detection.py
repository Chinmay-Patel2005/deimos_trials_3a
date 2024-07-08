import cv2
import numpy as np

# Check OpenCV version to determine correct import
if cv2.__version__.startswith('4'):
    from cv2 import aruco
else:
    import cv2.aruco as aruco

# Load the ArUco dictionary
aruco_dict = aruco.getPredefinedDictionary(aruco.DICT_6X6_250)
parameters = aruco.DetectorParameters()

# Open the video file
video_path = 'path_to_your_video.mp4'  # Change this to your video file path
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect markers
    corners, ids, rejectedImgPoints = aruco.detectMarkers(gray, aruco_dict, parameters=parameters)

    # Draw detected markers
    if ids is not None:
        frame = aruco.drawDetectedMarkers(frame, corners, ids)

    # Display the frame
    cv2.imshow('ArUco Marker Detection', frame)

    # Exit on 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
