from django.shortcuts import render
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from django.template import loader
from django.http import HttpResponse
from io import BytesIO
import base64
#import plotly.offline
#import plotly.graph_objects as go
from .utils import get_plot

# Create your views here.

def main_view(request) :
    chart = get_plot()
    return render(request,"main.html",{'chart': chart})

def nav(request) :
    return render(request, "nav.html")

def pca(request) :
    return render(request,"pca.html")

def knn(request) :
    return render(request,"KNN.html")

def nn(request) :
    return render(request,"nn.html")

def rtf(request) :
    return render(request,"rtf.html")

def svc(request) :
    return render(request,"svc.html")

def knnx(request,z) :
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn import metrics
    from sklearn.preprocessing import StandardScaler
    from sklearn.model_selection import train_test_split
    df_spam = pd.read_excel("spambase.xlsx")
    x = df_spam.drop('spam', 1)
    y = df_spam["spam"]
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20, random_state=40)
    scaler = StandardScaler()
    scaler.fit(x_train)
    x_train = scaler.transform(x_train)
    x_test = scaler.transform(x_test)
    # test
    x = scaler.transform(x)
    knn = KNeighborsClassifier(n_neighbors=z)
    knn.fit(x_train, y_train)
    y_pred = knn.predict(x_test)
    pres = metrics.accuracy_score(y_test,y_pred)
    print(str(pres * 100) + "%")
    return render(request,"knnx.html",context={"acc":pres,"k":z})

def rtfx(request,g) :
    from sklearn.preprocessing import StandardScaler
    from sklearn.model_selection import train_test_split
    from sklearn.ensemble import RandomForestClassifier
    from sklearn import metrics
    df_spam = pd.read_excel("spambase.xlsx")
    x = df_spam.drop('spam', 1)
    y = df_spam["spam"]
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20, random_state=40)
    scaler = StandardScaler()
    scaler.fit(x_train)
    x_train = scaler.transform(x_train)
    x_test = scaler.transform(x_test)
    # test
    x = scaler.transform(x)
    clf = RandomForestClassifier(n_estimators=g)
    clf.fit(x_train, y_train)
    y_pred = clf.predict(x_test)
    pres = metrics.accuracy_score(y_test, y_pred)
    return render(request,"rtfx.html",context={"acc":pres,"n_est":g})