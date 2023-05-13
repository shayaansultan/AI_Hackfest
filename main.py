from flask import Flask
import ocr, mongo

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'


if __name__ == '__main__':
    app.run(debug=True)