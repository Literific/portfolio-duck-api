from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from stock.models import Stock, Industry
from django.contrib.auth.models import User

class StockTests(APITestCase):

    def test_view_stocks(self):
        """
        Ensure we can view all objects
        """
        url = reverse('stock_api:stocklistcreate')
        response = self.client.get(url, format='json') # simulating browser (client)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    # create data for our api
    def create_stock(self):
        """
        Ensure we can create a new Stock object and view object
        """
        self.test_industry = Industry.objects.create(name='django')
        self.testuser1 = User.objects.create_user(
            username ='test_user1', password='12345678'
        )
        data = {
            "stock_id":"pfe", "industry": test_industry, "date":"2021-08-14", "open":"48.0", "close":"48.0", "high": "48.0", "low": "48.0", "volume": "3000.0", "twentydayavg": "48.0", "rsi": "30", "lstm": "52.0"
        }
        url = reverse('stock_api:stocklistcreate')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)