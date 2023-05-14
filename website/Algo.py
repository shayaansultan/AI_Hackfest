from flask import session
from pymongo import MongoClient
from AI_Hackfest import ocr


client = MongoClient('mongodb+srv://yuvbindal:Xww24MOIaDv7Xc3t@cluster0.xgajwdp.mongodb.net/?retryWrites=true&w=majority')
db = client['hackathon']
collection = db['fs.files']

def get_image_path():
    user_email = session['username']
    result = collection.find_one({"user_email": user_email})
    if result:
        return result['image_path']
    else:
        return None

image_path = f'/static/{get_image_path}'
text_dict = ocr.ocr_main(image_path)
print(text_dict)