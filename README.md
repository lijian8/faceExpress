# Installation
* First, you have to download the [data from the kaggle competition ](https://www.kaggle.com/c/challenges-in-representation-learning-facial-expression-recognition-challenge/data)

	`wget https://www.kaggle.com/c/challenges-in-representation-learning-facial-expression-recognition-challenge/download/fer2013.tar.gz`
	
* Unzip it to the local directory

    `tar -xvf fer2013.tar.gz`

* Clone this repo
	`git clone https://github.com/IdoKenan/faceExpress.git`

* Make sure you have the latest Theano (bleeding edge, this is necessary because apparently the official release doesn't have RELU units yet) 

    `sudo pip install --upgrade git+git://github.com/Theano/Theano.git`

* Install keras
	`pip install keras`

* Then, just run

    `python train_cnn.py`


*  Install matplotlib for display_image

    `pip install matplotlib`

