from flask import Flask, request, render_template
from PIL import Image
import numpy as np
from keras.models import load_model

app = Flask(__name__)

# Load the pre-trained model
model = load_model("CNN_Model\cat_or_dog_CNN.keras")

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

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'image' in request.files:
            image = request.files['image']
            image_proc = process_image(image)
            prediction = model.predict(image_proc)
            result = 'Dog' if prediction[0][0] >= 0.5 else 'Cat'
            return render_template('index.html', predict = result)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

