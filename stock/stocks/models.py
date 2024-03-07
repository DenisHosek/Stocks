from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Ticker(models.Model):
    ticker = models.CharField(max_length=6, unique=True) 
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    currency = models.CharField(max_length=5)
class Stock(models.Model):
    ticker = models.ForeignKey(Ticker, null=True, on_delete=models.CASCADE)
    name_stock = models.CharField(max_length=30)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name_stock

    class Meta:
        unique_together = [["ticker", "user"]]

