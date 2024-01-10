from django.shortcuts import render
from django.views import View
from .models import *
from .forms import CustomerRegistrationForm
from django.contrib import messages


# def home(request):
#  return render(request, 'app/home.html')
class ProductView(View):
    def get(self,request):
     topwears = Product.objects.filter(category='TW')
     bottomwears = Product.objects.filter(category='BW')
     mobiles = Product.objects.filter(category='M')
     laptop = Product.objects.filter(category="L")
     return render(request,'app/home.html',{'topwears':topwears,'bottomwears':bottomwears,'mobiles':mobiles,'laptop':laptop})

# def product_detail(request):
#  return render(request, 'app/productdetail.html')

class ProductDetailView(View):
    def get(self,request,pk):
     product = Product.objects.get(pk=pk)
     return render(request,'app/productdetail.html',{'product':product})



def add_to_cart(request):
 return render(request, 'app/addtocart.html')

def buy_now(request):
 return render(request, 'app/buynow.html')

def profile(request):
 return render(request, 'app/profile.html')

def address(request):
 return render(request, 'app/address.html')

def orders(request):
 return render(request, 'app/orders.html')

def change_password(request):
 return render(request, 'app/changepassword.html')



def mobile(request,data=None):
 if data==None:
    mobiles = Product.objects.filter(category='M')
 elif data=='vivo' or data=='samsung':
    mobiles = Product.objects.filter(category='M').filter(brand=data)
 elif data=='below':
    mobiles = Product.objects.filter(category='M').filter(discounted_price__lt = 10000)
 elif data=='above':
    mobiles = Product.objects.filter(category='M').filter(discounted_price__gt = 10000)
 return render(request, 'app/mobile.html',{'mobiles':mobiles})

def topwear(request,data=None):
      if data==None:
         topwear = Product.objects.filter(category='TW')
      elif data=='ahuja' or data=='buja':
         topwear = Product.objects.filter(category='TW').filter(brand=data)
      elif data=='below':
         topwear = Product.objects.filter(category='TW').filter(discounted_price__lt = 500)
      elif data=='above':
         topwear = Product.objects.filter(category='TW').filter(discounted_price__gt = 500)
      return render(request, 'app/topwear.html',{'topwear':topwear})

def bottomwear(request,data=None):
       if data==None:
             bottomwear = Product.objects.filter(category='BW')
       elif data=='denim' or data=='spyker':
             bottomwear = Product.objects.filter(category='BW').filter(brand=data)
       elif data=='below':
             bottomwear = Product.objects.filter(category='BW').filter(discounted_price__lt=500)
       elif data=='above':
             bottomwear = Product.objects.filter(category='BW').filter(discounted_price__gt=500)
       return render(request,'app/bottomwear.html',{'bottomwear':bottomwear})

def laptop(request,data=None):
       if data == None:
             laptop = Product.objects.filter(category='L')
       elif data == 'ASUS' or data == 'HP' or data == 'DELL' or data == 'LENOVO':
             laptop = Product.objects.filter(category='L').filter(brand=data)
       elif data == 'below':
             laptop = Product.objects.filter(category='L').filter(discounted_price__lt=60000)
       elif data == 'above':
             laptop = Product.objects.filter(category='L').filter(discounted_price__gt=60000)
       return render(request,'app/laptop.html',{'laptop':laptop})



# def login(request):
#  return render(request, 'app/login.html')

# def customerregistration(request):
#  return render(request, 'app/customerregistration.html')

class CustomerRegistraionView(View):
       def get(self,reqeust):
             form = CustomerRegistrationForm()
             return render(reqeust,'app/customerregistration.html',{'form':form})
       def post(self,request):
             form = CustomerRegistrationForm(request.POST)
             if form.is_valid():
                   messages.success(request,'Congratulations!! Registered Successfully')
                   form.save()

             return  render(request,'app/customerregistration.html',{'form':form})
       

def checkout(request):
 return render(request, 'app/checkout.html')
