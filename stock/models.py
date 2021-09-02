from django.db import models

from django.contrib.auth.models import User
from django.utils import timezone

class Industry(models.Model):
    
    class Meta:
        db_table = 'Industry'

    options = (
        ('technology', 'Technology'),
        ('consumer', 'Consumer'),
        ('health', 'Health')
    )

    name = models.CharField(max_length = 200, choices=options, default='technology')

    def __str__(self):
        return self.name

class Stock(models.Model):
    
    class Meta: 
        db_table = 'Stock'
        ordering = ('-date',)

    industry = models.ForeignKey(Industry, on_delete=models.PROTECT, related_name='Stock')

    stock_id = models.CharField(max_length = 255)
    date = models.DateField()
    date_slug = models.SlugField(max_length=250)
    open = models.FloatField()
    close = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    volume = models.FloatField()
    twentydayavg = models.FloatField()
    rsi = models.FloatField()
    lstm = models.FloatField()

    def __str__(self):
        return self.stock_id

    
class Brokerage(models.Model):
    
    class Meta:
        db_table = 'Brokerage'

    # custom model manager
    class BrokerageObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(name='vanguard')

    options = (
        ('fidelity', 'Fidelity'),
        ('etrade', 'Etrade'),
        ('robinhood', 'Robinhood'),
        ('vanguard', 'Vanguard'), 
        ('chase', 'Chase'), 
        ('others', 'Others'),
    )
    def __str__(self):
        return self.name

    name = models.CharField(
        max_length = 200, choices=options, default='others')
    opened_at = models.DateField(default='2020-01-01')

    objects = models.Manager() # default manager
    brokerageobjects = BrokerageObjects() # custom manager


# on how `on_delete` works - great explanation!
#  https://stackoverflow.com/a/38389488
class Portfolio(models.Model):
    class Meta: 
        db_table = 'Portfolio'

    user = models.ForeignKey(
        User, on_delete= models.CASCADE, related_name='Portfolio'
    )


    brokerage = models.ForeignKey(
        Brokerage, on_delete=models.SET_DEFAULT, default='others', related_name='Portfolio'
    )

    stock_id = models.ForeignKey(
        Stock, on_delete=models.SET_DEFAULT, default='cash', related_name='Portfolio'
    )

    number_of_shares = models.FloatField()
    avg_cost_of_shares = models.FloatField()
    date_updated = models.DateField()




