from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
import yfinance
import requests
from .forms import StockForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Stock


def index(request):
    ticker = Stock.objects.filter(user=request.user.id)
    return render(request, "index.html", {'ticker': ticker})

def singup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect("home")
    else:
        form = UserCreationForm()

    return render(request, "signup.html", {"form": form})


def change_pass(request):
    return render(request, "pass_change.html")

@login_required
def add_stock(request):
    if request.method == ("POST"):
        form = StockForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            messages.add_message(request, messages.INFO, "Stock ticker was add.")
            return redirect('home')
    else:
        form = StockForm()
    return render(request, 'add_stock.html', {'form':form})