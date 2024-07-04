from PIL import Image, ImageDraw
from matplotlib import pyplot as plt
import urllib.request
import requests
from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.ai.vision.imageanalysis.models import VisualFeatures
from azure.core.credentials import AzureKeyCredential

def ForegroundMatting(endpoint, key, image_file):
    # Define the API version and mode
    api_version = "2023-02-01-preview"
    mode="foregroundMatting"
    
    # Generate a foreground matte
    print('\nForeground Matting our image...')

    url = "{}computervision/imageanalysis:segment?api-version={}&mode={}".format(endpoint, api_version, mode)

    headers= {
        "Ocp-Apim-Subscription-Key": key, 
        "Content-Type": "application/json" 
    }

    image_url="https://www.newsnationnow.com/wp-content/uploads/sites/108/2024/05/664cbf44098e65.46285470.jpeg?w=2560&h=1440&crop=1"

    body = {
        "url": image_url,
    }

    response = requests.post(url, headers=headers, json=body)

    image=response.content
    with open("ForegroundMatting.png", "wb") as file:
        file.write(image)
    print('  Results saved in ForegroundMatting.png \n')

def main():
    global client
    endpoint = 'YOUR-ENDPOINT'
    key = 'YOUR-KEY'

    # Get image
    image_url = 'https://www.newsnationnow.com/wp-content/uploads/sites/108/2024/05/664cbf44098e65.46285470.jpeg?w=2560&h=1440&crop=1'
    urllib.request.urlretrieve(image_url,"image_file")
    image = Image.open("image_file")
    client = ImageAnalysisClient(
        endpoint=endpoint,
        credential=AzureKeyCredential(key)
    )

    ForegroundMatting(endpoint, key, image)

if __name__ == "__main__":
    main()