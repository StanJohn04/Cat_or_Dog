from flask import Flask, request, render_template, session
from PIL import Image
import os
import numpy as np
from keras.models import load_model

from werkzeug.utils import secure_filename

# Load the pre-trained model
model = load_model("CNN_Model\cat_or_dog_CNN.keras")
#Define upload folder path
UPLOAD_FOLDER = os.path.join('static', 'uploads')
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
#config upload folder
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# Define the process_image() function
def process_image(image):
    # Add your image preprocessing code here
    # Example code to resize and convert to grayscale
    img = Image.open(image)
    img = img.resize((150, 150))
    img = img.convert('L')
    img = np.array(img) / 255.0
    img = img.reshape(1, 150, 150, 1)
    return img
app.secret_key = 'KEY'
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'image' in request.files:
            image = request.files['image']
            ####
            image_filename = secure_filename(image.filename)
            image.save(os.path.join(app.config['UPLOAD_FOLDER'],image_filename))
            session['uploaded_img_file_path'] = os.path.join(app.config['UPLOAD_FOLDER'], image_filename)
            img_file_path = session.get('uploaded_img_file_path', None)
            ###

            image_proc = process_image(image)
            prediction = model.predict(image_proc)
            result = 'Dog' if prediction[0][0] >= 0.5 else 'Cat'
            return render_template('result.html', predict = result, predicted_image = img_file_path)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

