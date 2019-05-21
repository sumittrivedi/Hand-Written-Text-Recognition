import time as t
import os
from flask import Flask, render_template, request

# import our OCR function
from ocr_core import ocr_core
from hdr import hdr_predition
from hdr import hdr_accuracy
from hdr import hdr_img

# define a folder to store and later serve the images
UPLOAD_FOLDER = '/static/uploads/'

# allow files of a specific type
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app = Flask(__name__)

# function to check the file extension
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# route and function to handle the home page
@app.route('/')
def home_page():
    return render_template('index.html')

# route and function to handle the upload page
@app.route('/upload', methods=['GET', 'POST'])
def upload_page():
    start = time.time()
    if request.method == 'POST':
        # check if there is a file in the request
        if 'file' not in request.files:
            return render_template('upload.html', msg='No file selected')
        file = request.files['file']
        # if no file is selected
        if file.filename == '':
            return render_template('upload.html', msg='No file selected')

        if file and allowed_file(file.filename):

            # call the OCR function on it
            extracted_text = ocr_core(file)
            end = time.time()
            predition_time =round(end-start,3)
            # extract the text and display it
            return render_template('upload.html',
                                   msg='Successfully processed',
                                   predition_time=predition_time,
                                   extracted_text=extracted_text,
                                   img_src=UPLOAD_FOLDER + file.filename)
    elif request.method == 'GET':
        return render_template('upload.html')

# route and function to handle the digit page
@app.route('/digit', methods=['GET', 'POST'])
def digit_page():
    start = time.time()
    if request.method == 'POST':
        index = request.form['index']
        predition = hdr_predition(index)
        accuracy = hdr_accuracy()
        img_src=hdr_img(index)
        end = time.time()
        predition_time =round(end-start,3)
        # extract the text and display it
        return render_template('digit.html',
                                predition=predition,
                                accuracy=accuracy,
                                predition_time=predition_time,
                                img_src=img_src)
    elif request.method == 'GET':
        return render_template('digit.html')

if __name__ == '__main__':
	app.debug = True
	app.run()
