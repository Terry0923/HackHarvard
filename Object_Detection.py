import io
import os
from google.cloud import vision
from google.cloud.vision import types
from PIL import Image
import requests
from io import BytesIO

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="My First Project-854b30065e6e.json"

def findObjectLabels(url):
    # Instantiates a client
    client = vision.ImageAnnotatorClient()
    response = requests.get(url)
    image = types.Image(content=io.BytesIO(response.content).read())
    # Performs label detection on the image file
    response = client.label_detection(image=image)
    labels = response.label_annotations
    label_description_list = []
    for label in labels:
        label_description_list.append(label.description)
    return label_description_list
