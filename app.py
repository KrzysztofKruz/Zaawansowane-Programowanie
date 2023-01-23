from flask import Flask, render_template
import os

app = Flask(__name__)

picImage = os.path.join('Zdjecia')

app.config['IMG_DIRECTORY'] = picImage


@app.route('/')
def index():
    return "write /person_detection"


@app.route('/person_detection', methods=['GET'])
def person_detection():
    pic = os.path.join(app.config['IMG_DIRECTORY'], 'Ludzie1.jpg')
    return render_template("index.html", user_image=pic)


if __name__ == '__main__':
    app.run(debug=True, port=8000)
