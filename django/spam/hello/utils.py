from django.shortcuts import render
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from django.template import loader
from django.http import HttpResponse
from io import BytesIO
import base64
import plotly.express as px
from sklearn.decomposition import PCA

#import plotly.offline
#import plotly.graph_objects as go

def get_graph() :
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph


def get_plot() :
    df_spam = pd.read_excel("C:/Users/ikitof/Documents/django/spam/spambase.xlsx")
    x = df_spam.drop('spam', 1)
    y = df_spam["spam"]
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20, random_state=40)
    scaler = StandardScaler()
    scaler.fit(x_train)
    x_train = scaler.transform(x_train)
    x_test = scaler.transform(x_test)
    x = scaler.transform(x)
    df = pd.DataFrame(x_train, columns=['freq_make', 'freq_adress', 'freq_all', 'freq_3d', 'freq_our',
                                        'freq_over', 'freq_remove', 'freq_internet', 'freq_order', 'freq_mail',
                                        'freq_receive', 'freq_will', 'freq_people', 'freq_report',
                                        'freq_addresses', 'freq_free', 'freq_business', 'freq_email',
                                        'freq_you', 'freq_credit', 'freq_your', 'freq_font', 'freq_000',
                                        'freq_money', 'freq_hp', 'freq_hpl', 'freq_george', 'freq_650',
                                        'freq_lab', 'freq_labs', 'freq_telnet', 'freq_857', 'freq_data',
                                        'freq_415', 'freq_85', 'freq_technology', 'freq_1999', 'freq-parts',
                                        'freq_pm', 'freq_direct', 'freq_cs', 'freq_meeting', 'freq_original',
                                        'freq_project', 'freq_re', 'freq_edu', 'freq_table', 'freq_conference',
                                        'freq_;', 'freq_(', 'freq_[', 'freq_!', 'freq_$', 'freq_#',
                                        'cap_average', 'cap_longest', 'cap_tot'])
    n_components = len(df.columns)
    # PCA.
    pca = PCA(n_components=2)
    components = pca.fit_transform(x_train)
    fig = px.scatter(components, x=0, y=1, color=y_train)
    fig.show()
    #plt.switch_backend("AGG")
    #plt.figure(figsize=(10,5))
    #plt.tight_layout()
    graph = get_graph()
    return graph

# Create your views here.