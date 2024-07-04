from PIL import Image, ImageDraw
from matplotlib import pyplot as plt
import urllib.request
import requests
from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.ai.vision.imageanalysis.models import VisualFeatures
from azure.core.credentials import AzureKeyCredential

def AnalyzeImage(image_url, client):
    print('\nAnalyzing image...')
    # Get result with specified features to be retrieved
    result = client.analyze_from_url(
        image_url=image_url,
        visual_features=[
            VisualFeatures.CAPTION,
            VisualFeatures.OBJECTS,
            VisualFeatures.PEOPLE,
            VisualFeatures.TAGS,
            VisualFeatures.READ,
            VisualFeatures.DENSE_CAPTIONS,
        ],
        language='en'
    )
    # Get image captions
    if result.caption is not None:
        print("\nCaption:")
        print(" Caption: '{}' (confidence: {:.2f}%)".format(result.caption.text, result.caption.confidence * 100))

    # Get image dense captions
    if result.dense_captions is not None:
        print("\nDense Captions:")
        for caption in result.dense_captions.list:
            print(" Caption: '{}' (confidence: {:.2f}%)".format(caption.text, caption.confidence * 100))

    # Get image tags
    if result.tags is not None:
        print("\nTags:")
        for tag in result.tags.list:
            print(" Tag: '{}' (confidence: {:.2f}%)".format(tag.name, tag.confidence * 100))
    
    # Get objects in the image
    if result.objects is not None:
        print("\nObjects in image:")
        urllib.request.urlretrieve('https://www.newsnationnow.com/wp-content/uploads/sites/108/2024/05/664cbf44098e65.46285470.jpeg?w=2560&h=1440&crop=1', "file_name")
        image = Image.open("file_name")
        fig = plt.figure(figsize=(image.width/100, image.height/100))
        plt.axis('off')
        draw = ImageDraw.Draw(image)
        color = 'cyan'

        for detected_object in result.objects.list:
            print(" {} (confidence: {:.2f}%)".format(detected_object.tags[0].name, detected_object.tags[0].confidence * 100))

            r = detected_object.bounding_box
            bounding_box = ((r.x, r.y), (r.x + r.width, r.y + r.height)) 
            draw.rectangle(bounding_box, outline=color, width=3)
            plt.annotate(detected_object.tags[0].name,(r.x, r.y), backgroundcolor=color)

        plt.imshow(image)
        plt.tight_layout(pad=0)
        outputfile = 'result_objects.jpg'
        fig.savefig(outputfile)
        print('  Results saved in', outputfile)
    
    # Get people in the image
    if result.people is not None:
        print("\nPeople in image:")
        urllib.request.urlretrieve('https://www.newsnationnow.com/wp-content/uploads/sites/108/2024/05/664cbf44098e65.46285470.jpeg?w=2560&h=1440&crop=1', "file_name")
        image = Image.open("file_name")
        fig = plt.figure(figsize=(image.width/100, image.height/100))
        plt.axis('off')
        draw = ImageDraw.Draw(image)
        color = 'cyan'

        for detected_people in result.people.list:
            # Draw object bounding box
            r = detected_people.bounding_box
            bounding_box = ((r.x, r.y), (r.x + r.width, r.y + r.height))
            draw.rectangle(bounding_box, outline=color, width=3)

            # Return the confidence of the person detected
            print(" {} (confidence: {:.2f}%)".format(detected_people.bounding_box, detected_people.confidence * 100))

        # Save annotated image
        plt.imshow(image)
        plt.tight_layout(pad=0)
        outputfile = 'result_people.jpg'
        fig.savefig(outputfile)
        print('  Results saved in', outputfile)

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
        
    # Analyze image
    AnalyzeImage(image_url, client)

if __name__ == "__main__":
    main()