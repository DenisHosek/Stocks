from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def index(request):
    #response = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=demo')
    #data = response.json()
    return render(request, "index.html")

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

def account(request):
    return render(request, "account.html")
