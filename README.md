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


## Deploying our model


# Team Members
  * [Stan Johnson](https://github.com/StanJohn04)
  * [Brian Haynes](https://github.com/brianphaynes)
  * [Kelsey Abbey](https://github.com/kelseyabbey)
  * [Toan Nguyen](https://github.com/Toan88Nguyen)
