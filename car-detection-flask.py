import flask
from flask import Flask,render_template, request, send_file
import cardetect
from tensorflow.keras.preprocessing import image
import os
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
from tensorflow.keras.applications.resnet50 import preprocess_input
model=load_model("model_resnet50.h5")

app= Flask(__name__,template_folder='meow')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/cardetect', methods=['GET','POST'])
def cardetect():
    return render_template('prediction.html')

@app.route('/detect', methods=['GET','POST'])
def detect():
    print(request.files)
    img1= request.files['upload']
    img1.save("uploaded.jpg")
    img=image.load_img("uploaded.jpg",target_size=(224,224))
    x=image.img_to_array(img)
    x=x/255
    x=np.expand_dims(x,axis=0)
    img_data=preprocess_input(x)
    model.predict(img_data)
    a=np.argmax(model.predict(img_data), axis=1)
    b=int(a)
    x=""
    if (b==0):
        x=x+"Audi"
    elif (b==1):
        x=x+"Bmw"    
    elif (b==2):
        x=x+"Bugatti"
    elif(b==3):
        x=x+"Ferrari"
    elif(b==4):
        x=x+"Maserati"
    elif(b==5):
        x=x+"Mercedes"
    elif(b==6):
        x=x+"RollsRoyce"
    elif(b==7):
        x=x+"Tesla"
    elif(b==8):
        x=x+"Toyota"
    elif(b==9):
        x=x+"Volkswagen"  
    os.remove("uploaded.jpg")
    return render_template('prediction.html',x=x)    


if __name__ == '__main__':
    app.run(debug=True, port=8080)