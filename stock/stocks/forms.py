from django.forms import ModelForm

from .models import Stock

class StockForm(ModelForm):
    class Meta:
        model = Stock
        exclude = ['user']

    def clean_ticker(self):
        data = self.cleaned_data['ticker']
        ticker = data.upper()
        return ticker
