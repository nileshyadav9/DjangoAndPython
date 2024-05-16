from django.http import HttpResponse
from django.shortcuts import render
from .models import Product


# map /products -> index
def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})
    # return HttpResponse('Hello World')


def new(request):
    return HttpResponse('New Product')
