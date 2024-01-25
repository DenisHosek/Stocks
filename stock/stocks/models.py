from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Stock(models.Model):
    ticker = models.CharField(max_length=6)
    name_stock = models.CharField(max_length=30)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name_stock

    def clean_ticker(self):
        data = self.cleaned_data['ticker']
        ticker = data.lower()
        return ticker


    class Meta:
        unique_together = [["ticker", "user"]]