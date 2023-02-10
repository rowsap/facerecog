#import google.cloud.vision

from google.cloud import vision

image_uri = 'C:\\Users\\rowsa\\Downloads\\7jvnrhhnfws41.jpg'

client = vision.ImageAnnotatorClient()
image = vision.Image() # Py2+3 if hasattr(vision, 'Image') else vision.types.Image()
image.source.image_uri = image_uri

response = client.label_detection(image=image)

print('Labels (and confidence score):')
print('=' * 30)
for label in response.label_annotations:
    print(label.description, '(%.2f%%)' % (label.score*100.))