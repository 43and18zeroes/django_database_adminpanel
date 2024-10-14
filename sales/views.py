from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Customer
from django.views.generic.detail import DetailView

# Create your views here.

class CustomerListView(ListView):
    model = Customer
    template_name = "sales/list.html"
    
class CustomerListSearchView(CustomerListView):
    def get_queryset(self):
        name = self.kwargs.get("name")
        return Customer.objects.filter(first_name__icontains=name)
    
class CustomerDetailView(DetailView):
    model = Customer
    template_name = 'sales/detail.html'