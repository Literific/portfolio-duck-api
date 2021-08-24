from django.urls import path
from .views import StockList, StockDetail, IndustryList

# Url path pattern reference: 
# https://www.webforefront.com/django/accessurlparamstemplates.html

app_name = 'stock_api'

urlpatterns = [
    path('stock/<int:pk>', StockDetail.as_view(), name='detailcreate'),
    path('stock', StockList.as_view(), name='listcreate'),
    path('industry', IndustryList.as_view(), name='listcreate')
]