from django import forms

from .models import Stock

class StockForm(forms.Form):
    ticker = forms.CharField(label="Ticker", max_length=6)
    name_stock = forms.CharField(label="Name of Ticker", max_length=30)

    def clean_ticker(self):
        data = self.cleaned_data['ticker']
        ticker = data.upper()
        return ticker

class SearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=30, required=False)