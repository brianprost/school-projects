import cv2
import sys
from pathlib import Path


def menu():
    image_directory = "photo/img/"
    image_path = image_directory + "a_famous_photo.jpeg"
    image_name = Path(image_path).stem
    image = cv2.imread(image_path)
    image_grayed = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faces = detect_faces(image_grayed)

    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (299, 9, 20), 2)

    status = cv2.imwrite(
        f"{image_directory}{image_name}_faces_detected.jpeg", image)
    print("Image faces_deteced.jpg written to filesystem: ", status)


def get_pic():
    pass


def detect_faces(image):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +
                                         "haarcascade_frontalface_default.xml"
                                         )
    faces = face_cascade.detectMultiScale(
        image,
        scaleFactor=1.3,
        minNeighbors=3,
        minSize=(75, 75)
    )
    print("Found {0} Faces!".format(len(faces)))
    return faces


def filter_pic():
    pass


if __name__ == "__main__":
    menu()
