import flask
from flask import Flask,render_template, request, send_file

app= Flask(__name__,template_folder='meow')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, port=8080)