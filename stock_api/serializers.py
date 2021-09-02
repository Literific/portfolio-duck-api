from rest_framework import serializers
from stock.models import Brokerage, Stock, Industry, Portfolio


class IndustrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Industry
        fields =('id','name',)

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ('id', 'stock_id', 'date', 'industry', 'open', 'close', 'high', 'low','volume', 'twentydayavg', 'rsi', 'lstm')

class BrokerageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brokerage
        fields = ('id', 'name', 'opened_at')
    
class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = ('id', 'user', 'brokerage', 'stock_id', 'number_of_shares', 'avg_cost_of_shares', 'date_updated')
