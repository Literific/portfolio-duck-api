from rest_framework import generics 
from stock.models import Stock, Industry
from .serializers import StockSerializer, IndustrySerializer


# https://www.django-rest-framework.org/
# what data do you want to serialize from database?
# https://www.django-rest-framework.org/tutorial/1-serialization/
class StockList(generics.ListCreateAPIView):
    queryset = Stock.objects.all()
    # queryset = Stock.stockobjects.all() # using custom manager
    serializer_class = StockSerializer

class StockDetail(generics.RetrieveDestroyAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

class IndustryList(generics.ListCreateAPIView):
    queryset = Industry.objects.all()
    serializer_class = IndustrySerializer



""" Concrete View Classes
#CreateAPIView
Used for create-only endpoints.
#ListAPIView
Used for read-only endpoints to represent a collection of model instances.
#RetrieveAPIView
Used for read-only endpoints to represent a single model instance.
#DestroyAPIView
Used for delete-only endpoints for a single model instance.
#UpdateAPIView
Used for update-only endpoints for a single model instance.
##ListCreateAPIView
Used for read-write endpoints to represent a collection of model instances.
RetrieveUpdateAPIView
Used for read or update endpoints to represent a single model instance.
#RetrieveDestroyAPIView
Used for read or delete endpoints to represent a single model instance.
#RetrieveUpdateDestroyAPIView
Used for read-write-delete endpoints to represent a single model instance.
"""