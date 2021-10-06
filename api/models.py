from django.db import models

# Create your models here.

class Soda(models.Model):
    product_name = models.CharField(max_length=15)
    description = models.TextField()
    cost = models.DecimalField(max_digits=14, decimal_places=2, help_text='in US dollars $')
    quantity = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.product_name
