from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.ai.vision.imageanalysis.models import VisualFeatures
from azure.core.credentials import AzureKeyCredential

client = ImageAnalysisClient(
    endpoint="https://analyseimages-prnvpwr2612.cognitiveservices.azure.com/",
    credential=AzureKeyCredential("18ffa797cfa84f7fbbf79b2e3eada2f8")
)

result = client.analyze_from_url(
    image_url="https://statics.foxsports.com/www.foxsports.com/content/uploads/2024/06/2024-06-30_Soccer-Live-Blog_Spain-vs-Georgia_16x9.jpg",
    visual_features=[VisualFeatures.CAPTION, 
                     VisualFeatures.READ,
                     VisualFeatures.OBJECTS,
                     VisualFeatures.READ,
                     VisualFeatures.TAGS,
                     VisualFeatures.SMART_CROPS,
                     VisualFeatures.DENSE_CAPTIONS],
    gender_neutral_caption=True,
    language="en",
)

print(result)