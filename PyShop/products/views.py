from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Product, UserNumberTest


# map /products -> index
def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})
    # return HttpResponse('Hello World')


def new(request):
    return HttpResponse('New Product')


def user_number_test2(request):
    return HttpResponse('UserNumber')


def user_number_test(request):
    if request.method == 'POST':
        username = request.POST.get('name')
        usernumber = request.POST.get('number')

        # Save into DB
        insertObj = UserNumberTest(usernumber=usernumber, username=username)
        insertObj.save()

        return JsonResponse({'success': True})
    else:
        return render(request, 'user_number_test.html')
