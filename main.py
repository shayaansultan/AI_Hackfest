from flask import Blueprint, Flask, render_template, request, session, send_from_directory, url_for, session
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import SubmitField
from flask_pymongo import PyMongo
from flask_uploads import UploadSet, IMAGES, configure_uploads
from bson import ObjectId
import os
from datetime import datetime
from pymongo import MongoClient
import website.ocr as ocr
import website.analytics as analytics
from website import create_app
import website.mongo as mong


app = create_app()

app.config['MONGO_URI'] = 'mongodb+srv://yuvbindal:Xww24MOIaDv7Xc3t@cluster0.xgajwdp.mongodb.net/hackathon?retryWrites=true&w=majority'
app.config['UPLOADED_PHOTOS_DEST'] = '/Users/yuvvvvv/Desktop/MLH_AI/AI_Hackfest/website/static'

mongo = PyMongo(app)

photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)

class UploadForm(FlaskForm):
    photo = FileField(
        validators = [
            FileAllowed(photos, 'Only images are allowed!'),
            FileRequired('File field should not be empty!')
        ]
    )
    submit = SubmitField('Upload')

@app.route('/scan/<filename>')
def get_file(filename):
    return send_from_directory(app.config['UPLOADED_PHOTOS_DEST'], filename)

@app.route('/scan', methods=['POST'])
def image_analysis():
    user_email = session['username']
    #result = mongo.db['fs.files'].find_one({"user_email": user_email})
    image_path = 'RECIEPT2_2.png'
    text_dict = ocr.ocr_main(image_path)
    mong.insert_receipt(str(user_email), '2022-01-02', text_dict)
    #print('Uploaded to database')

    df = analytics.create_dataframe(user_email)

    table_html = df.to_html(index=False)

    return render_template('home.html', table_html=table_html)

    #print(df)

    # do something with text_dict, e.g., save it to a database
    #print(text_dict)
    


    #return render_template('scan.html', text_dict=text_dict)

    



@app.route('/scan',methods =['GET','POST'])
def upload_image():
    form = UploadForm()
    if form.validate_on_submit():
        photo = form.photo.data
        filename = photos.save(photo)

        # Get file extension
        file_ext = os.path.splitext(filename)[1].lower()

        # Generate unique file ID
        file_id = ObjectId()

        # Save file to MongoDB
        with open(os.path.join(app.config['UPLOADED_PHOTOS_DEST'], filename), 'rb') as f:
            mongo.db.fs.files.insert_one({
                '_id': file_id,
                'contentType': f'image/{file_ext}',
                'metadata': {
                    'email': session.get('email'),
                    'username': session.get('username'),
                },
            })
            mongo.save_file(filename, f)

        file_url = url_for('get_file', filename=filename)
    else:
        file_url = None

    return render_template('scan.html', form=form, file_url=file_url)


if __name__ == '__main__':
    app.run(debug=True)

