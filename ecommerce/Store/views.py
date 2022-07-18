import re
from django.shortcuts import render , redirect , HttpResponseRedirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .serializers import CategorySerializer, ProductSerializer
from .models import Category, Product
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

# class Cart(View):
#     def get(self , request):
#         ids = list(request.session.get('cart').keys())
#         products = Product.get_products_by_id(ids)
#         print(products)
#         return render(request , 'Cart.html' , {'products' : products} )


# class CheckOut(View):
#     def post(self, request):
#         address = request.POST.get('address')
#         phone = request.POST.get('phone')
#         customer = request.session.get('customer')
#         cart = request.session.get('cart')
#         products = Product.get_products_by_id(list(cart.keys()))
#         print(address, phone, customer, cart, products)

#         for product in products:
#             print(cart.get(str(product.id)))
#             order = Order(customer=Customer(id=customer),
#                           product=product,
#                           price=product.price,
#                           address=address,
#                           phone=phone,
#                           quantity=cart.get(str(product.id)))
#             order.save()
#         request.session['cart'] = {}

#         return redirect('cart')

# class Index(View):

#     def post(self , request):
#         product = request.POST.get('product')
#         remove = request.POST.get('remove')
#         cart = request.session.get('cart')
#         if cart:
#             quantity = cart.get(product)
#             if quantity:
#                 if remove:
#                     if quantity<=1:
#                         cart.pop(product)
#                     else:
#                         cart[product]  = quantity-1
#                 else:
#                     cart[product]  = quantity+1

#             else:
#                 cart[product] = 1
#         else:
#             cart = {}
#             cart[product] = 1

#         request.session['cart'] = cart
#         print('cart' , request.session['cart'])
#         return redirect('homepage')



#     def get(self , request):
#         # print()
#         return HttpResponseRedirect(f'/store{request.get_full_path()[1:]}')

# def store(request):
#     cart = request.session.get('cart')
#     if not cart:
#         request.session['cart'] = {}
#     products = None
#     categories = Category.get_all_categories()
#     categoryID = request.GET.get('category')
#     if categoryID:
#         products = Product.objects.filter(pk=categoryID)
#     else:
#         products = Product.objects.all();

#     data = {}
#     data['products'] = products
#     data['categories'] = categories

#     print('you are : ', request.session.get('email'))
#     return render(request, 'index.html', data)


# class OrderView(View):


#     def get(self , request ):
#         customer = request.session.get('customer')
#         orders = Order.get_orders_by_customer(customer)
#         print(orders)
#         return render(request , 'Orders.html'  , {'orders' : orders})

class CategoryView(APIView):

    def get(self, request):
        user_count = Category.objects.all()
        serializer = CategorySerializer(user_count, many=True)
        return Response({'category': serializer.data})

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'status': 403, 'errors': serializer.errors, 'message': 'something went wrong'})
        serializer.save()
        return Response({'status': 200, 'payload': serializer.data, 'message': 'user registration success'})

def index(request):
    return render(request,'index.html')

def login(request):
    return render(request, 'Login.html')


def signup(request):
    return render(request, 'Signup.html')


class ProductView(APIView):
    def get(self, request):
        user_count = Product.objects.all()
        serializer = ProductSerializer(user_count, many=True)
        return Response({'category': serializer.data})
