from django.db import models

# Create your models here.

from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    newsletter_abo = models.BooleanField(default=True)
    email_address = models.EmailField(max_length=30, blank=True, default="")
    account = models.FloatField(blank=True, null=True)
    
    class Meta:
        verbose_name="Banana"
        verbose_name_plural="Many Customersss"
        ordering=["-first_name"]
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    def save(self):
        self.account = 4325234
        return super().save()
    
class Product(models.Model):
    name = models.CharField(max_length=30)
    price = models.FloatField()
    
    def __str__(self):
        return f"{self.name} {self.price}"


class Bill(models.Model):
    total_amount = models.FloatField()
    is_paid = models.BooleanField(default=False)

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE) # one-to-many
    products = models.ManyToManyField(Product, through="Producttype") # many-to-many (through())
    bill = models.OneToOneField(Bill, on_delete=models.CASCADE) # one-to-one
    
class Producttype(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    type_name = models.CharField(max_length=300)
    
    def __str__(self):
        return f"{self.type_name}"
    
    # def save(self, *args, **kwargs):
    #     print("saved")
    #     super.save(*args, **kwargs)
