import boto3
import os
import cv2
import sys
from pathlib import Path
import requests
import re
import shutil


def menu():
    image_url = get_image_url()


    # lambda from here on out
    image_from_internet = download_image_from_internet(image_url)

    # if not image_from_internet[0]:
    #     # implement
    #     return 404
    # image_directory = "photo/img/"
    # image_path = image_directory + "a_famous_photo.jpeg"
    # image_name = Path(image_path).stem
    # image = cv2.imread(image_path)
    # image_grayed = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # faces = detect_faces(image_grayed)

    # for (x, y, w, h) in faces:
    #     cv2.rectangle(image, (x, y), (x+w, y+h), (20, 9, 229), 4)

    # status = cv2.imwrite(
    #     f"{image_directory}{image_name}_faces_detected.jpeg", image)
    # print("Image faces_deteced.jpg written to filesystem: ", status)


def get_image_url():
    while True:
        image_url = input("Enter an image URL: ")

        image_url_regex = re.compile(
            r'^(?:http|ftp)s?://'
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'
            r'localhost|'
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
            r'(?::\d+)?'
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)

        if re.match(image_url_regex, image_url) is not None:
                return image_url
        print("Invalid URL. Please enter the full web address. ex: https://website.com/image/my_image.jpeg")


def download_image_from_internet(image_url):
    filename = Path(image_url).name
    response = requests.get(image_url)

    if response.status_code != 200:
        return [False, "There was an error accessing your image.", None]
    response.raw.decode_content = True

    with open(filename,'wb') as f:
        shutil.copyfileobj(response.raw, f)
        
    s3 = boto3.resource('s3')
    s3.meta.client.upload_file(filename, 'edu.umgc.sdev400.prost.homework4', filename)
    
    os.remove(filename)
    return [True, "File successfully downloaded", filename]




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


if __name__ == "__main__":
    menu()
