from django.urls import path
from .views import StockList, StockDetail, IndustryList, PortfolioList, BrokerageList, PortfolioDetail

# Url path pattern reference: 
# https://www.webforefront.com/django/accessurlparamstemplates.html

app_name = 'stock_api'

urlpatterns = [
    path('stock/<int:pk>', StockDetail.as_view(), name='detailcreate'),
    path('stock', StockList.as_view(), name='stocklistcreate'),
    path('industry', IndustryList.as_view(), name='industrylistcreate'),
    path('portfolio', PortfolioList.as_view(), name='portfoliolistcreate'),
    path('portfolio/<int:pk>', PortfolioDetail.as_view(), name='portfoliodetailcreate'),
    path('brokerage', BrokerageList.as_view(), name='brokeragelistcreate'),
]