# Installation
First, you have to download the [data from the kaggle competition ](https://www.kaggle.com/c/challenges-in-representation-learning-facial-expression-recognition-challenge/data) and unzip it to the local directory
    ``tar -xvf fer2013.tar.gz``

Make sure you have the latest Theano (bleeding edge, this is necessary because apparently the official release doesn't have RELU units yet) 

Then, just run
    `` python train_cnn.py``
