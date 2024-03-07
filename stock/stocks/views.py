from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
import yfinance as yf
import requests
from .models import Stock, Ticker
from .forms import StockForm, SearchForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponseRedirect


def index(request):
    ticker = Stock.objects.filter(user=request.user.id)
    return render(request, "index.html", {'ticker': ticker})

@login_required
def stocks(request):
    stocks = Stock.objects.filter(user=request.user.id)
    form = SearchForm(request.GET)
    if form.is_valid():
        query = form.cleaned_data['query']
        stocks = stocks.filter(Q(name_stock__icontains = query) | Q(ticker__ticker__icontains = query))
    return render(request, "stocks.html", {'stocks': stocks, 'form':form})
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

@login_required
def change_pass(request):
    return render(request, "pass_change.html")

@login_required
def add_stock(request):
    if request.method == "POST":
        form = StockForm(request.POST)
        if form.is_valid():
            tick = yf.Ticker(form.cleaned_data['ticker'])
            info = tick.info
            ticker, created = Ticker.objects.get_or_create(ticker=form.cleaned_data['ticker'])

            ticker.price = info.get("currentPrice",0)
            ticker.currency = info.get('currency', '')
            ticker.save()
            stock, created = Stock.objects.get_or_create(
                ticker = ticker,
                user = request.user,
                defaults={'name_stock': form.cleaned_data['name_stock']}
            )
            return redirect("stock_list")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = StockForm()
    return render(request, 'add_stock.html', {'form':form})

@login_required
def stock_info(request, stock_id):
    stock = get_object_or_404(Stock, id = stock_id, user_id = request.user.id)
    ticker = yf.Ticker(str(stock.ticker.ticker))
    dividends = ticker.dividends.to_dict()
    info = ticker.info
    currency = info.get('currency')
    web = info.get('website')
    price = info["currentPrice"]
    EPS = info["trailingEps"]
    sales = 1
    PE = round(price / EPS, 2)
    PS = round(price / sales, 2)
    PBV = round(price / sales, 2)
    return render(request, 'stock.html', {'ticker':ticker, 'stock':stock, 'divid': dividends, 'currency':currency, 'web':web, 'all':info, 'pe': PE})

@login_required
def refresh(request):
    for ticker in Ticker.objects.all():
        t = yf.Ticker(ticker.ticker)
        ticker.price = t.info.get("currentPrice")
        ticker.save()
    return redirect('stock_list')
