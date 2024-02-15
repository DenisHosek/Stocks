from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
import yfinance as yf
import requests
from .forms import StockForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Stock


def index(request):
    ticker = Stock.objects.filter(user=request.user.id)
    return render(request, "index.html", {'ticker': ticker})

def stocks(request):
    ticker = Stock.objects.filter(user=request.user.id)
    return render(request, "stocks.html", {'ticker': ticker})
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

@login_required
def stock_info(request, stock_id):
    stock = get_object_or_404(Stock, id = stock_id)
    ticker = yf.Ticker(str(stock.ticker))
    dividends = ticker.dividends.to_dict()
    info = ticker.info
    currency = info.get('currency')
    web = info.get('website')
    return render(request, 'stock.html', {'ticker':ticker, 'stock':stock, 'divid': dividends, 'currency':currency, 'web':web})
