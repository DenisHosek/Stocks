from django.contrib import admin

from .models import Stock, Ticker
# Register your models here.
@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    pass




@admin.register(Ticker)
class TickerAdmin(admin.ModelAdmin):
    pass
