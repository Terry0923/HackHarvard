from google_images_download import google_images_download
from PIL import Image
import imghdr
import os

def findImageUrls(query, limit):
    download_response = google_images_download.googleimagesdownload()
    arguments = {"keywords": query,
				"format": "jpg",
				"limit":limit,
				"print_urls":False,
				"size": "medium",
                "no_download":True,
				"aspect_ratio": "panoramic"}
    dirname = os.path.dirname(__file__)
    try:
        responses = download_response.download(arguments)
    except FileNotFoundError:
        print("Image not found!")
    return responses[0].get(query)
