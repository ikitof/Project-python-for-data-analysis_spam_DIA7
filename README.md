# About the django API
# How to lauch
The django file include the django projet and the virtual environnement for python (.env).
To start the environnement go to the depositery with the project and type .env\Scripts\activate.bat (or source .env\Scripts\activate)
to launch the project move to the spam directory and type py manage.py runserver or on linux (python manage.py runserver)
# How to use 
go to http://127.0.0.1:8000/ on any browser and use the naviguation bar to move as you wish between the section.
In addition you can go to url such as http://127.0.0.1:8000/knn/45 to test the accuracy of the knn function with a specified value for the number of neighbours.
It also works with the random tree forest and the n_estimator http://127.0.0.1:8000/rtf/45

# Notebook
This notebook contains a data visualisation part, three different sklearn algorithms applied to the dataset to predict classification. A Keras Sequential Neural Network and a mixed solution between ANN and RTF with an accuracy of 96%.

# Powerpoint Presentation
This powerpoint essentialy is a README, you'll understand our thought process and what we did in detail.
Thank you for your time.
