from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
import yfinance
import requests


def index(request):
    #url = 'https://newsapi.org/v2/top-headlines?category=business&apiKey=1ef0301a838743b2ba3585b9e71d8b10'
    #response = requests.get(url)
    #data = response.json()

    #articles = data['articles']

    #context = {
    #    'articles': articles
    #}

    return render(request, "index.html")#, context)

def stock(request):

    return render(request, 'stock.html')

def singup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect('home')
    else:
        form = UserCreationForm()

    return render(request, "signup.html", {"form" : form})

def change_pass(request):
    return render(request, 'pass_change.html')