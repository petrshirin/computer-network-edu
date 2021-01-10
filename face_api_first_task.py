import cognitive_face as CF
from PIL import Image

def cat_face(face_data: dict) -> None:
    image = Image.open('face_api_data/img1.jpg')
    cropped = image.crop((face_data['left'],
                          face_data['top'],
                          face_data['left'] + face_data['width'],
                          face_data['top'] + face_data['height']))
    cropped.save('face_api_data/result.png')

KEY = 'f12693bc12c7479d829a57734f145e24'  # Replace with a valid Subscription Key here.
CF.Key.set(KEY)

BASE_URL = 'https://westeurope.api.cognitive.microsoft.com/face/v1.0/'  # Replace with your regional Base URL
CF.BaseUrl.set(BASE_URL)

img_url = 'https://cdn1.fullpicture.ru/wp-content/uploads/2014/12/Idealnoe-muzhskoe-litso-5.jpg'
result = CF.face.detect(img_url)
cat_face(result[0]['faceRectangle'])






