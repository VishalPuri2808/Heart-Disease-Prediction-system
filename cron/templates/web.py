#description:

import pandas as pd 
from    sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier


import streamlit as st

st.write("""
Heart disease Prediction System
""")


df =pd.read_csv(r'C:\Users\Hacker\Downloads\cron\hdps\dataset.csv')

st.subheader('Data Information')
st.dataframe(df)

st.write(df.describe())

chart =st.bar_chart(df)

X = df.iloc[:,0:13].values
Y = df.iloc[:,-1].values


X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.25, random_state=0)

def get_user_input():
    
    age = st.sidebar.slider('Age',0,70,18)
    se = st.sidebar.slider('sex',0,1,0)
    cp = st.sidebar.slider('chest pain',0,3,0)
    trestbps =st.sidebar.slider('Blood pressure',94,200,130)
    chol = st.sidebar.slider('cholestrol',126,564,541)
    fbs = st.sidebar.slider('Blood sugar',0,1,0)
    restecg = st.sidebar.slider('resting electrocardiographic results',0,1,0)
    thalach = st.sidebar.slider('maximum heart rate achieved',71,202,153)
    exang = st.sidebar.slider('exercise induced angina',0,1,0)
    oldpeak	= st.sidebar.slider('ST depression induced by exercise relative to rest',0.00,6.20,0.80)
    slope	= st.sidebar.slider('the slope of the peak exercise ST segment',0,2,2)
    ca	= st.sidebar.slider('number of major vessels',0,4,0)
    tha = st.sidebar.slider('thal ',0,4,2)
    
    user_data = {'Age' : age,
             'sex' : se,
             'chest pain' : cp,
             'Blood pressure' : trestbps,
             'cholestrol' : chol,
             'Blood sugar' : fbs,
             'resting electrocardiographic results' : restecg,
             'maximum heart rate achieved' : thalach,
             'exercise induced angina' : exang,
             'ST depression induced by exercise relative to rest' : oldpeak,
             'the slope of the peak exercise ST segment' : slope,
             'number of major vessels' : ca,
             'thal' : tha
             }
    features =pd.DataFrame(user_data, index =[0])
    return features



user_input = get_user_input()

st.subheader('User Input:')
st.write(user_input)

DecisionTreeClassifier = DecisionTreeClassifier()
DecisionTreeClassifier.fit(X_train, Y_train)

st.subheader('Model Test Accuracy Score:')
st.write( str(accuracy_score(Y_test, DecisionTreeClassifier.predict(X_test))*100)+'%')

prediction = DecisionTreeClassifier.predict(user_input)
st.subheader('classification')
st.write(prediction)





