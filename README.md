
# Cat_or_Dog

## Project Proposal
Use a CNN to determine if an image is of a cat or a dog. Build out a dashboard to allow a user to input a picture of a cat or a dog and have the model predict which it is.

Link to [dataset](https://www.kaggle.com/datasets/unmoved/30k-cats-and-dogs-150x150-greyscale)

## Building and Training our CNN model
### Toolkit
Follow the links below to learn more about the tools used for this project
 * [keras](https://keras.io/api/)
     * [model](https://keras.io/api/models/)
     * [layers](https://keras.io/api/layers/)
     * [callbacks](https://keras.io/api/callbacks/)
     * [optimizers](https://keras.io/api/optimizers/)
     * [tuner](https://keras.io/api/keras_tuner/)
 * [TensorFlow - ImageDataGenerator](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/image/ImageDataGenerator)
 * [sklearn](https://scikit-learn.org/stable/modules/classes.html)
   * [train_test_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html)
### Building our model
We built and trained our model in Google Colab using an A100 GPU as it was a very resource intensive process.
Our notebook can be found [here](https://github.com/StanJohn04/Cat_or_Dog/blob/main/CNN_Model/Model_Build%26Train_COLAB.ipynb)

The data was loaded into the Colab session straight from the kaggle API - directions on how to do so can be found [here](https://www.kaggle.com/discussions/general/156610)
![image](https://github.com/StanJohn04/Cat_or_Dog/assets/121142680/93175039-9345-462f-b803-4f41dbfc8d4f)

Using ImageDataGenerator we labeled all the images in the dataset. 0 = cat, 1 = Dog. We then used train-test-split to split our data into training and test sets:
![image](https://github.com/StanJohn04/Cat_or_Dog/assets/121142680/3a8404a0-509f-48b8-9fa4-f5fa1c030395)

We built a base model that achieved 73% accuracy:
![image](https://github.com/StanJohn04/Cat_or_Dog/assets/121142680/ea8bf23f-156e-47d5-b11a-3c2f49c7de02)

After some expirementing with different hyper parameters, activation functions, and number of layers we were able to achieve 75% accuracy:
![image](https://github.com/StanJohn04/Cat_or_Dog/assets/121142680/cd9ef7ad-20f7-4c4f-be83-45cf94d162fd)
![image](https://github.com/StanJohn04/Cat_or_Dog/assets/121142680/aa18a98e-d85f-49c8-859e-9e378322c49a)

After noticing and increase in accuracy from manipulating the different parameters of the model, we decided to let keras-tuner run through the different hyper parameters to fine tune the model...

First we set up data augmentation parameters to make our dataset more generalized:
![image](https://github.com/StanJohn04/Cat_or_Dog/assets/121142680/b114b8c5-ae2e-4cd4-bd52-c0963c97a9de)

Then we let keras tuner run different trial using different values for dropout coefficient, filter numbers, number of layers and number of units in each layer:
![image](https://github.com/StanJohn04/Cat_or_Dog/assets/121142680/0f39cb59-7f8a-42ea-80b0-14b3f9fdba88)

The tuner returned the best model:

![image](https://github.com/StanJohn04/Cat_or_Dog/assets/121142680/5959f8a3-7e36-4acb-ba55-35eeb20284bf)

With accuracy on the test data of 90.87%!
![image](https://github.com/StanJohn04/Cat_or_Dog/assets/121142680/c0dc59f1-1109-4045-a8de-8a0af9fdcc6b)



## Testing our model
### Toolkit:
Follow the links below to learn more about the tools used for this project
 * [keras-load_model](https://keras.io/api/)
 * [TensorFlow - image](https://www.tensorflow.org/api_docs/python/tf/image)
 * [numpy](https://numpy.org/doc/)
 * [matplotlib](https://matplotlib.org/stable/index.html)
 * [urlib_request](https://docs.python.org/3/library/urllib.request.html)
 * [io.BytesIO](https://docs.python.org/3/library/io.html)
### Testing the model in jupyter notebook:
To test our model we wrote a function that preprocesses an uploaded image and then runs it through the model to predict whether its an image of a cat or a dog. The notebook for this can be found [here](https://github.com/StanJohn04/Cat_or_Dog/blob/main/CNN_Model/Model_Test.ipynb)

We tested the model with images downloaded from google and images of our own pets. All of the test images were NOT part of the training or test data used in the previous section.

![image](https://github.com/StanJohn04/Cat_or_Dog/assets/121142680/e011f2db-2afe-45ea-aadb-3aad6fa85efa)


## Deploying our model
 ![image](https://github.com/StanJohn04/Cat_or_Dog/assets/122308689/176e6e9f-e51d-4068-89ac-9d68d04e0fed)

 
First we import the necessary tools
 
![image](https://github.com/StanJohn04/Cat_or_Dog/assets/122308689/3d751f32-8789-4c29-bdd6-6a204babf2a7)


We load in the pre-trained model that can predict whether an image contains a cat or a dog.
The model is loaded from the specified path.

![image](https://github.com/StanJohn04/Cat_or_Dog/assets/122308689/3559d160-cec3-4285-9eb9-ab9f6f0c7db5)


Next we define where uploaded files will be stored.
UPLOAD_FOLDER: The path where uploaded files will be saved.
ALLOWED_EXTENSIONS: A set of allowed file extensions.



Then we create a Flask app instance that will serve as our web application. Then we configure the app to use the upload folder we defined earlier.




Image Processing Function:
We define a function called process_image to prepare an uploaded image for the model.
The function resizes the image to 150x150, converts it to grayscale, normalizes pixel values, and reshapes it for the model.


 
Main Route:
Then we create a main page ('/') to deal with users' requests.
Inside the index() function:
If a user uploads an image (POST request) it takes the uploaded image and saves it in the upload folder.
Then it adjusts the image for the model, asks the model if it's a cat or dog and shows the result on the result.html page with the image.
 ![Uploading image.png…]()

Run the app
Summary
This code sets up a Flask web app where users can upload images. The images are processed, and a pre-trained model predicts whether they're cats or dogs. The result, along with the uploaded image, is then displayed on the result page.


# Team Members
  * [Stan Johnson](https://github.com/StanJohn04)
  * [Brian Haynes](https://github.com/brianphaynes)
  * [Kelsey Abbey](https://github.com/kelseyabbey)
  * [Toan Nguyen](https://github.com/Toan88Nguyen)
