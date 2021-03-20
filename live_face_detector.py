from detector import *

# Start the webcam
webcam = cv.VideoCapture(0)

# Capture images in a loop
frame_present, frame = webcam.read()
while frame_present and not(cv.waitKey(15) & 0xFF == ord('d')):
    frame_present, frame = webcam.read()
    detect_faces(frame)
    cv.imshow('Faces detcted', frame)

webcam.release()
cv.destroyAllWindows()