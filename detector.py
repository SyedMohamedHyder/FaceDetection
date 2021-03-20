import cv2 as cv

# Initialize the classifier
# haarcascade_frontalface_default.xml contains data of the pre-trained classifier
face_detector = cv.CascadeClassifier('haarcascade_frontalface_default.xml')

def detect_faces(frame):
    # Convert the image to grayscale image
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # Find all the faces from the grayscaled image using the face detector
    rects = face_detector.detectMultiScale(gray)

    for x, y, w, h in rects:
        cv.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 255), thickness=3)

if __name__ == '__main__':
    # Read the image array of the group photo
    img = cv.imread('group1.jpg')

    # Call the function to detect faces in the image
    detect_faces(img)

    # Display the image
    cv.imshow('Faces Detected', img)

    # Wait till any key is pressed
    cv.waitKey(0)

    # Destroy all the window
    cv.destroyAllWindows()