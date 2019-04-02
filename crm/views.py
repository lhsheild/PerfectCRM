from django.shortcuts import render
from django.views import View


# Create your views here.
class Index(View):
    @staticmethod
    def get(request):
        return render(request, 'index.html')


class CustomerList(View):
    def get(self, request):
        return render(request, 'sales/customers.html')
