from rest_framework import serializers
from stock.models import Stock, Industry


class IndustrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Industry
        fields =('id','name',)

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ('id', 'stock_id', 'date', 'industry', 'open', 'close', 'high', 'low','volume', 'twentydayavg', 'rsi', 'lstm')
