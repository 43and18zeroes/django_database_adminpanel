from django.db import models

# Create your models here.

from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    newsletter_abo = models.BooleanField(default=True)
    email_address = models.EmailField(max_length=30, blank=True, default="")
    account = models.FloatField(blank=True, null=True)
    
class Product(models.Model):
    name = models.CharField(max_length=30)
    price = models.FloatField()
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE) # one-to-many
    products = models.ManyToManyField(Product)
    
class Bill(models.Model):
    total_amount = models.FloatField()
    is_paid = models.BooleanField(default=False)