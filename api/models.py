from django.db import models
from datetime import date


# Create your models here.

class Soda(models.Model):
    product_name = models.CharField(max_length=15)
    description = models.TextField()
    cost = models.DecimalField(max_digits=4, decimal_places=2, help_text='in US dollars $')
    quantity = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.product_name

class Order(models.Model) :
    product_name = models.CharField(max_length=15)
    cost = models.DecimalField(max_digits=4, decimal_places=2, help_text='in US dollars $')
    quantity = models.PositiveSmallIntegerField()
    card_number = models.CharField(max_length=100)
    security_code = models.CharField(max_length=3)
    expiration_date = models.DateField(("Date"), default=date.today,help_text='use format MM/DD/YY')
    zip_code = models.CharField(max_length=10)

    def __str__(self):
        return self.product_name