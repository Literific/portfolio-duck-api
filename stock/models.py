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

    industry = models.ForeignKey(Industry, on_delete=models.PROTECT)

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
        max_length = 200, choices=options, default='fidelity')
    objects = models.Manager() # default manager
    brokerageobjects = BrokerageObjects() # custom manager



