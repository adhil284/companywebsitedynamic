from django.contrib import admin
from .models import People,Peoplelist,Product,Productlist

# Register your models here.
admin.site.register(People,Peoplelist)
admin.site.register(Product,Productlist)