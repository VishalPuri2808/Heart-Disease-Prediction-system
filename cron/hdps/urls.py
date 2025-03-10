from django.contrib import admin
from django.urls import path,include
from hdps import views

urlpatterns =[
    path("",views.index,name="home"),
    path("signup.html",views.signup,name="signup"),
    path("login.html",views.login,name="login"),
    path("entry.html",views.entry,name="entry"),
    path("patient.html",views.patient,name="patient"),
    path("service.html",views.service,name="service"),
    path("contact.html",views.contact,name="contact"),
    path("about.html",views.about,name="about"),
    path("index.html",views.index,name="index"),
    path("aptmt.html",views.aptmt,name="aptmt"),
    path("temp.html",views.temp,name="temp"),

     


 ]

  