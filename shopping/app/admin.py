from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Product)
class AdminModelProduct(admin.ModelAdmin):
    list_display = ['title','selling_price','discounted_price','description','brand','category','product_image']

@admin.register(Customer)
class CustomerAdminModel(admin.ModelAdmin):
    list_display = ['id','Name','locality','city','zipcode','state']

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display=['user','product','quantity']
@admin.register(OrderPlaced)
class OrderPlaceAdmin(admin.ModelAdmin):
    list_display=['user','customer','product','quantity','ordered_date','status']
