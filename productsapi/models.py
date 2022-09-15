from django.db import models

# Create your models here.
class ProductItems(models.Model):
    title=models.CharField(max_length=120)
    price=models.PositiveIntegerField()
    rating=models.PositiveIntegerField()
    category=models.CharField(max_length=100)
    description=models.CharField(max_length=250)
