from django.contrib import admin
from . import models

@admin.register(models.Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ('stock_id', 'date', 'date_slug', 'industry', 'open', 'close', 'high', 'low','volume', 'twentydayavg', 'rsi', 'lstm')
    prepopulated_fields = {'date_slug': ('date',),}

# Register your models here.

admin.site.register(models.Industry)