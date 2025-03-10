from django.shortcuts import render
import pandas as pd 
from    sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from .models import records

import streamlit as st
import csv



# Create your views here.
def index(request):
 
    return render(request,"index.html")
def about(request):
    return render(request,"about.html")  
def aptmt(request):
    return render(request,"aptmt.html")     
def contact(request):
    return render(request,"contact.html")
def service(request):
    return render(request,"service.html")   

def temp(request):
    if request.method == 'POST':

       
        # writer.writerow(["pemail","pname","pmob","paddr","page","psex","pcp","ptrestbps","pchol","pfbs","prestecg","pthalach","pexang","poldpeak","pslope","pca","presult"])
        username=request.POST.get('email2')
        name=request.POST.get('name2')
        
        mob=request.POST.get('mob2')
        addr=request.POST.get('addr')
        doct1=request.POST.get('doc')

        print(doct1)


        patient_detail=pd.read_csv("details.csv")
        list(patient_detail['Name'])

        for row,pname in enumerate(patient_detail['Name']):
            if name==pname:
                
                page=patient_detail['age'][row]
                psex=patient_detail['se'][row]
                pcp=patient_detail['cp'][row]
                ptrestbps=patient_detail['trestbps'][row]
                pchol=patient_detail['chol'][row]
                pfbs=patient_detail['fbs'][row]
                prestecg=patient_detail['restecg'][row]
                pthalach=patient_detail['thalach'][row]
                pexang=patient_detail['exang'][row]
                poldpeak=patient_detail['oldpeak'][row]
                pslope=patient_detail['slope'][row]
                pca=patient_detail['ca'][row]
                presult=patient_detail['result'][row]
                
                break

        with open("apt.csv",mode="a",newline="") as f:
        
            writer = csv.writer(f,delimiter=",")
            writer.writerows([[username,name,mob,addr,page,psex,pcp,ptrestbps,pchol,pfbs,prestecg,pthalach,pexang,poldpeak,pslope,pca,presult,doct1]])
            print("Registration successful!")
        


    return render(request,"login.html")       




def signup(request):
    return render(request,"signup.html")
def patient(request):
    print("xaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
    if request.method == 'POST':
        df =pd.read_csv('dataset.csv')
        X = df.iloc[:,0:13].values
        Y = df.iloc[:,-1].values
        
        X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.25, random_state=0)

        model = DecisionTreeClassifier()
        model.fit(X_train, Y_train)

        nm=request.POST.get('name')
        email1=request.POST.get('email1')
        age = request.POST.get('ag')
        se = request.POST.get('gen')
        cp = request.POST.get('cp')
        trestbps =request.POST.get('bp')
        chol = request.POST.get('cho')
        fbs = request.POST.get('bs')
        restecg = request.POST.get('res')
        thalach = request.POST.get('rat')
        exang = request.POST.get('ind')
        oldpeak	= request.POST.get('peak')
        slope	= request.POST.get('slope')
        ca	= request.POST.get('vessels')
        tha = request.POST.get('thal')

        pred = model.predict([[age,se,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,tha]])

        result2=""
        if pred==[1]:
            result2="Positive"
        else:
            result2="Negative"
        
        with open("details.csv",mode="a",newline="") as f:
            
            writer = csv.writer(f,delimiter=",")
            writer.writerows([[nm,age,se,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,tha,result2]])
            print("entry successful!")


            patient_details=pd.read_csv("user.csv")
            list(patient_details['username'])
            for row,eml in enumerate(patient_details['username']):
                if email1==eml:
                    ad=patient_details['addr'][row]
                    p=patient_details['mob'][row]
                    b=[]
                    for i,type in enumerate(patient_details['type']):
                        if type=="Doctor":
                            d_add=patient_details['addr'][i]
                            if ad==d_add:
                                d_name=patient_details['username'][i]
                                b.append(d_name)
                    
        return render(request,"patient.html" ,{"r":result2,"name2":nm,"sex2":se,"email2":email1,"ad2":ad,"mob2":p ,"b":b})
    
    return render(request,"patient.html")    


def login(request):
    if request.method == 'POST':    
       
        with open("user.csv",mode="a",newline="") as f:
            
            writer = csv.writer(f,delimiter=",")
            # writer.writerow(["username","password","type","mob","addr"])
            username=request.POST.get('email')
            password=request.POST.get('password1')
            password2=request.POST.get('password2')
            typ=request.POST.get('typ')
            mob=request.POST.get('mob')
            addr=request.POST.get('addr')
                
            if password==password2:
                writer.writerows([[username,password,typ,mob,addr]])
                print("Registration successful!")
            else:print("Please try again..")


    
    return render(request,"login.html")        


def entry(request):
    if request.method == 'POST':
        username=request.POST.get('email')
        password=request.POST.get('password')
        typ=request.POST.get('typ')

        with open("user.csv",mode="r") as f:
            reader = csv.DictReader(f,delimiter=",")
            for row in reader:
                if row['username']==username and row['password']==password and row['type']==typ and row['type']=='Patient':
                    print("You are Logged in!")
                    return render(request,"entry.html",{"email1":username})
                if row['username']==username and row['password']==password and row['type']==typ and row['type']=='Doctor':
                    d=[]
                    p_details=pd.read_csv('apt.csv')
                   
                    
                        
                    for i in range(p_details.shape[0]):
                        if p_details['doctor'][i]==username:
                            temp=p_details.loc[i]
                            d.append(dict(temp))
                       

                              
                         

    
                
                    print("You are Logged in!")
                    return render(request,"aptmt.html",{"email1":username,"det":d})

            print("please try again!")
            return render(request,'login.html' )

     
    else:
        return render(request,"entry.html")    

               


    
    
    
