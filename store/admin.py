from django.contrib import admin
from .models import Category,Customer,Product,Order,Test
# Register your models here.

admin.site.register(Customer)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Test)