import flask
from flask import Flask,render_template, request, send_file
import cardetect

app= Flask(__name__,template_folder='meow')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/cardetect', methods=['GET','POST'])
def cardetect():
    img1= request.files['file-upload']
    b=cardetect.detect(img1)
    return render_template('prediction.html',b=b)



if __name__ == '__main__':
    app.run(debug=True, port=8080)