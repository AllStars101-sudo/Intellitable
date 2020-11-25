#Intellitable by Chris and Joshua
import json
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import Home, UserInputFormModel
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout, authenticate, login
from django.urls import reverse
from .forms import NewUserForm
import csv
import pandas as pd
import sklearn
from sklearn import svm, preprocessing
import random
from django.views.decorators.cache import cache_page
from main.forms import SubjectInput
from django.contrib import messages
from requests import request
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import datetime
import matplotlib.pyplot as plt
import io
import urllib, base64


# Create your views here.

def homepage(request):
    return render(request,
                  'main/home.html',
                  context={"home":Home.objects.all})


def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            login(request, user)
            return redirect("main:login")

        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])

            return render(request = request,
                          template_name = "main/register.html",
                          context={"form":form})

    form = NewUserForm
    return render(request = request,
                  template_name = "main/register.html",
                  context={"form":form})


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('usrinp')

    form = AuthenticationForm()
    return render(request = request,
                    template_name = "main/login.html",
                    context={"form":form})
                    

def main(request):
    return render(request,
                  'main/main.html',
                  context={"home":Home.objects.all})


def logout_request(request):
    logout(request)
    return redirect("main:home")


def test(request):
    if request=='POST':
        dict1=request.POST
        with open('studentdata.csv','a') as csvfile:
            wrt = csv.csvwriter(csvfile)
            for key, value in dict1.items():
             wrt.writrow([key,value])
    return render(request,'main/test.html')


def testml(request):
    return render(request,
                  'main/testml.html',
                  context={"home":Home.objects.all})




def scheduleAlgo(request):
    givenData=pd.read_csv('~\OneDrive\Desktop\example.csv')
    df = pd.DataFrame(givenData)
    df['Mean']=df.mean(axis=1)
    df = df.sort_values(by="Mean", ascending=False)
    df.set_index("Subject", inplace = True)
    firstSubject = df.index[0]
    secondSubject = df.index[1]
    thirdSubject = df.index[2]
    fourthSubject = df.index[3]
    fifthSubject = df['Mean'].idxmin()
    if fifthSubject==fourthSubject:
        fourthSubject=df.index[4]
    subjectList=[fifthSubject,fourthSubject,thirdSubject,secondSubject,firstSubject]

    subjectSelection = random.choices(subjectList, weights=(20,18,17,16,15),k=5)
    print(subjectSelection)
    return render(request, 'main/testml.html', 
    {
    'firstSubject': subjectSelection[0],
    'secondSubject':subjectSelection[1],
    'thirdSubject':subjectSelection[2],
    'fourthSubject':subjectSelection[3],
    'fifthSubject':subjectSelection[4],
    }) 


def score(request):
    givenData=pd.read_csv('~\OneDrive\Desktop\example.csv')
    df = pd.DataFrame(givenData)
    df['Mean']=df.mean(axis=1)
    df = df.sort_values(by="Mean", ascending=False)
    df.set_index("Subject", inplace = True)
    

    df = sklearn.utils.shuffle(df) # shuffling data to avoid any biases that may emerge b/c of some order.

    X = df.values
    X = preprocessing.scale(X)
    y = df["Mean"].values

    test_size = 1

    X_train = X[:-test_size]
    y_train = y[:-test_size]

    X_test = X[-test_size:]
    y_test = y[-test_size:]

    clf = svm.SVR()

    clf.fit(X_train, y_train)

    for X,y in list(zip(X_test, y_test))[:10]:
        predictedScore = int(clf.predict([X])[0])
        print(predictedScore)
    return render(request, "main/testml.html", {
            'score':predictedScore})


def usrinp(request):
    return render(request,"main/usrinp.html")

def usrinp_save(request):
    username=request.POST.get("username")
    subject1=request.POST.get("subject1")
    sub1exam1=request.POST.get("sub1exam1")
    sub1exam2=request.POST.get("sub1exam2")
    sub1exam3=request.POST.get("sub1exam3")
    sub1exam4=request.POST.get("sub1exam4")
    sub1exam5=request.POST.get("sub1exam5")
    subject2=request.POST.get("subject2")
    sub2exam1=request.POST.get("sub2exam1")
    sub2exam2=request.POST.get("sub2exam2")
    sub2exam3=request.POST.get("sub2exam3")
    sub2exam4=request.POST.get("sub2exam4")
    sub2exam5=request.POST.get("sub2exam5")
    subject3=request.POST.get("subject3")
    sub3exam1=request.POST.get("sub3exam1")
    sub3exam2=request.POST.get("sub3exam2")
    sub3exam3=request.POST.get("sub3exam3")
    sub3exam4=request.POST.get("sub3exam4")
    sub3exam5=request.POST.get("sub3exam5")
    subject4=request.POST.get("subject4")
    sub4exam1=request.POST.get("sub4exam1")
    sub4exam2=request.POST.get("sub4exam2")
    sub4exam3=request.POST.get("sub4exam3")
    sub4exam4=request.POST.get("sub4exam4")
    sub4exam5=request.POST.get("sub4exam5")
    subject5=request.POST.get("subject5")
    sub5exam1=request.POST.get("sub5exam1")
    sub5exam2=request.POST.get("sub5exam2")
    sub5exam3=request.POST.get("sub5exam3")
    sub5exam4=request.POST.get("sub5exam4")
    sub5exam5=request.POST.get("sub5exam5")

    listsub1 = [subject1, subject2,subject3,subject4,subject5]
    listsub2 = [int(sub1exam1),int(sub2exam1),int(sub3exam1),int(sub4exam1),int(sub5exam1)]
    listsub3 = [int(sub1exam2),int(sub2exam2),int(sub3exam2),int(sub4exam2),int(sub5exam2)]
    listsub4 = [int(sub1exam3),int(sub2exam3),int(sub3exam3),int(sub4exam3),int(sub5exam3)]
    listsub5 = [int(sub1exam4),int(sub2exam4),int(sub3exam4),int(sub4exam4),int(sub5exam4)]
    listsub6 = [int(sub1exam5),int(sub2exam5),int(sub3exam5),int(sub4exam5),int(sub5exam5)]
    df = pd.DataFrame(list(zip(listsub1,listsub2,listsub3,listsub4,listsub5,listsub6)), columns=['Subject','Year1','Year2','Year3','Year4','Year5'])
    df['Mean']=df.mean(axis=1)
    df = df.sort_values(by="Mean", ascending=False)
    df.set_index("Subject", inplace = True)
    firstSubject = df.index[0]
    secondSubject = df.index[1]
    thirdSubject = df.index[2]
    fourthSubject = df.index[3]
    fifthSubject = df['Mean'].idxmin()
    if fifthSubject==fourthSubject:
        fourthSubject=df.index[4]
    subjectList=[fifthSubject,fourthSubject,thirdSubject,secondSubject,firstSubject]

    subjectSelection = random.choices(subjectList, weights=(20,18,17,16,15),k=5)

    df = sklearn.utils.shuffle(df) # shuffling data to avoid any biases that may emerge b/c of some order.

    X = df.values
    X = preprocessing.scale(X)
    y = df["Mean"].values

    test_size = 1

    X_train = X[:-test_size]
    y_train = y[:-test_size]

    X_test = X[-test_size:]
    y_test = y[-test_size:]

    clf = svm.SVR()

    clf.fit(X_train, y_train)

    for X,y in list(zip(X_test, y_test))[:10]:
        predictedScore = int(clf.predict([X])[0])
        print(predictedScore)

    currentTime = datetime.datetime.now()
    currentTime.hour
    if currentTime.hour < 12:
        goodResult='Good morning'
    elif 12 <= currentTime.hour < 18:
        goodResult='Good afternoon'
    else:
        goodResult='Good evening'

    return render(request, "main/main.html", {
        'predictedScore':predictedScore,     
        'firstSubject': subjectSelection[0],
        'secondSubject':subjectSelection[1],
        'thirdSubject':subjectSelection[2],
        'fourthSubject':subjectSelection[3],
        'fifthSubject':subjectSelection[4],
        'username_to_show':username,
        'goodResult':goodResult,
        'fifthSubject_to_show':fifthSubject})


