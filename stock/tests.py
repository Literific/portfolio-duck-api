from django.test import TestCase
from django.contrib.auth.models import User
from stock.models import Stock, Industry, Brokerage

class Test_Create_Stock(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_industry = Industry.objects.create(name='health')
        testuser1 = User.objects.create_user(
            username='test_user1', password='123456789'
        )
        test_stock = Stock.objects.create(
            stock_id='pfe', industry=test_industry, date='2021-08-14', open=48.0, close=48.0, high=48.0, low=48.0, volume=3000.0, twentydayavg=48.0, rsi=30, lstm=52.0
        )

    def test_stock_content(self):
        stk = Stock.objects.get(id=1)
        ind = Industry.objects.get(id=1)
        name = f'{stk.stock_id}'
        industry = f'{stk.industry}'
        self.assertEqual(name, 'pfe')
        self.assertEqual(industry, 'health')
        self.assertEqual(str(ind), 'health')
