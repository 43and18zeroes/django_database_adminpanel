from django.contrib import admin
from .models import Customer, Bill, Product, Producttype, Order

# Register your models here.


class CustomerAdmin(admin.ModelAdmin):
    list_filter = ["first_name", "last_name"]
    readonly_fields = ['account']

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Bill)
admin.site.register(Product)
admin.site.register(Producttype)
admin.site.register(Order)
