from website import create_app, mongo
from flask import Blueprint, Flask, render_template, request, session, send_from_directory, url_for, session
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import SubmitField
from flask_pymongo import PyMongo
from flask_uploads import UploadSet, IMAGES, configure_uploads
from bson import ObjectId
import os
from datetime import datetime
import website.mongo as mong
from website.auth import get_username

print('hi')


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


@app.route('/scan',methods =['GET','POST'])
def upload_image():
    form = UploadForm()
    if form.validate_on_submit():
        user_email =  get_username() # get user email from session or wherever you're storing it
        file = form.photo.data  # get the uploaded file
        filename = photos.save(file)  # save the file locally
        file_url = url_for('get_file', filename=filename)  # get the URL of the saved file
        
        # create a document to insert into the database
        metadata = {
            'filename': filename,
            'user_email': get_username(),
            'uploaded_at': datetime.utcnow()
        }
        file_id = mongo.db.receiptImages.insert_one(metadata).inserted_id  # insert the document and get the ID
        file_ext = os.path.splitext(filename)[1]
        # update the document with the binary data of the file
        if file_id:

            mongo.db.fs.files.update_one(
                {'_id': file_id},
                {'$set': {'contentType': 'image/png', 'metadata': metadata}},
                upsert=True
            )
        else:
            raise Exception("File could not be uploaded")
    else:
        file_url = None

    return render_template('scan.html', form=form, file_url=file_url)

if __name__ == '__main__':
    app.run(debug=True)

