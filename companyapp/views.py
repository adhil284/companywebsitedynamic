from django.shortcuts import render
from .models import People
from .models import Product

# Create your views here.
def people(request):

    context = {}
    context['peoples'] = People.objects.all()
    return render(request,'companyapp/people.html',context)
def products(request):
    context = {}
    context['products'] = Product.objects.all()
    return render(request, 'companyapp/products.html', context)

def home(request):
    context = {}
    return render(request, 'companyapp/home.html', context)

def contact(request):
    context = {}
    return render(request, 'companyapp/contact.html', context)
