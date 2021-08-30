from rest_framework import generics 
from stock.models import Stock, Industry, Portfolio, Brokerage
from .serializers import StockSerializer, IndustrySerializer, PortfolioSerializer, BrokerageSerializer
from rest_framework.permissions import SAFE_METHODS, BasePermission, IsAdminUser, DjangoModelPermissions


class PortfolioUserWritePermission(BasePermission):
    message = "Editing portfolio components is restricted to the account holder only."

    def has_object_permission(self, request, view, obj):
        # if any of options are GET, OPTION, or HEAD
        if request.method in SAFE_METHODS:
            return True

        return obj.user == request.user


# https://www.django-rest-framework.org/
# what data do you want to serialize from database?
# https://www.django-rest-framework.org/tutorial/1-serialization/
class StockList(generics.ListCreateAPIView):
    # add authentication level 
    permission_classes = [DjangoModelPermissions]
    queryset = Stock.objects.all()
    # queryset = Stock.stockobjects.all() # using custom manager
    serializer_class = StockSerializer

class StockDetail(generics.RetrieveDestroyAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

class IndustryList(generics.ListCreateAPIView):
    queryset = Industry.objects.all()
    serializer_class = IndustrySerializer
class PortfolioList(generics.ListCreateAPIView):
    permission_classes = [DjangoModelPermissions]
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer

# https://www.django-rest-framework.org/api-guide/filtering/
# Filtering against query parameters
# http://example.com/api/purchases?username=denvercoder9
class PortfolioDetail(generics.RetrieveUpdateDestroyAPIView, PortfolioUserWritePermission):
    # only the user of the portfolio can update the portfolio
    permission_classes = [PortfolioUserWritePermission]
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer

    # def get_queryset(self):
    #     """
    #     This view should return a list of all the stocks
    #     for the currently authenticated user
    #     """
    #     queryset = Portfolio.objects.all()
    #     this_user = self.request.query_params.get('user')
    #     print("this_user", this_user)
    #     if this_user is not None:
    #         queryset = queryset.filter(user=this_user)
    #     return queryset

class BrokerageList(generics.ListCreateAPIView):
    queryset = Brokerage.objects.all()
    serializer_class = BrokerageSerializer


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