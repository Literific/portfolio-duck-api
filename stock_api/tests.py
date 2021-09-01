from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from stock.models import Stock, Industry, Brokerage, Portfolio
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
            "stock_id":"pfe", "industry": self.test_industry, "date":"2021-08-14", "open":"48.0", "close":"48.0", "high": "48.0", "low": "48.0", "volume": "3000.0", "twentydayavg": "48.0", "rsi": "30", "lstm": "52.0"
        }
        url = reverse('stock_api:stocklistcreate')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # test custom permission
    def test_portfolio_update_correct_user(self):

        client = APIClient()

        self.test_industry = Industry.objects.create(name='django')
        self.test_user1 = User.objects.create_user(
            username ='test_user1', password = '12345678'
        )
        self.test_brokerage = Brokerage.objects.create(name='fidelitytest')
        self.test_stock = Stock.objects.create(
            industry=self.test_industry, stock_id='tsla', date='2020-01-01', \
            date_slug='2020-01-01', open=123.45, close=123.45, high=987.65, \
            low='1.23', volume='12345.0', twentydayavg=456.78, rsi=980.1, lstm=654.32
        )
        
        test_portfolio = Portfolio.objects.create(
            user=self.test_user1, brokerage=self.test_brokerage, stock_id=self.test_stock, \
            number_of_shares = '132', avg_cost_of_shares = '456.78', date_updated='2021-08-30'
        ) 

        client.login(username=self.test_user1.username, password='12345678')
        url = reverse(('stock_api:portfoliodetailcreate'), kwargs={'pk': 1})
        response = client.put(
            url, {
                "id": 1, 
                "user": 1, 
                "brokerage": 1, 
                "stock_id": 1, 
                "number_of_shares": 1.00, 
                "avg_cost_of_shares": 460.5, 
                "date_updated": "2020-05-21",
            }, format='json'
        )
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    # test custom permission
    def test_portfolio_update_wrong_user(self):

        client = APIClient()

        self.test_industry = Industry.objects.create(name='django')
        self.test_user1 = User.objects.create_user(
            username ='test_user1', password = '12345678'
        )
        self.test_user2 = User.objects.create_user(
            username ='test_user2', password = '12345678'
        )
        self.test_brokerage = Brokerage.objects.create(name='fidelitytest')
        self.test_stock = Stock.objects.create(
            industry=self.test_industry, stock_id='tsla', date='2020-01-01', \
            date_slug='2020-01-01', open=123.45, close=123.45, high=987.65, \
            low='1.23', volume='12345.0', twentydayavg=456.78, rsi=980.1, lstm=654.32
        )
        
        test_portfolio = Portfolio.objects.create(
            user=self.test_user1, brokerage=self.test_brokerage, stock_id=self.test_stock, \
            number_of_shares = '132', avg_cost_of_shares = '456.78', date_updated='2021-08-30'
        ) 

        client.login(username=self.test_user2.username, password='12345678')
        url = reverse(('stock_api:portfoliodetailcreate'), kwargs={'pk': 1})
        response = client.put(
            url, {
                "id": 1, 
                "user": 1, 
                "brokerage": 1, 
                "stock_id": 1, 
                "number_of_shares": 1.00, 
                "avg_cost_of_shares": 460.5, 
                "date_updated": "2020-05-21",
            }, format='json'
        )
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

