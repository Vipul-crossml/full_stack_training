import email
from urllib import response
from django.contrib.auth.hashers import check_password
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate, login
import json
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from Customer.serializers import *
# Create your views here.
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import api_view
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny


# class Login(View):
#     return_url = None
#     def get(self , request):
#         Login.return_url = request.GET.get('return_url')
#         return render(request , 'Login.html')

#     def post(self , request):
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         customer = Customer.get_customer_by_email(email)
#         error_message = None
#         if customer:
#             flag = check_password(password, customer.password)
#             if flag:
#                 request.session['customer'] = customer.id

#                 if Login.return_url:
#                     return HttpResponseRedirect(Login.return_url)
#                 else:
#                     Login.return_url = None
#                     return redirect('homepage')
#             else:
#                 error_message = 'Email or Password invalid !!'
#         else:
#             error_message = 'Email or Password invalid !!'

#         print(email, password)
#         return render(request, 'Login.html', {'error': error_message})

# def logout(request):
#     request.session.clear()
#     return redirect('login')

# class Signup(View):
#     def get(self, request):
#         return render(request, 'Signup.html')

#     def post(self, request):
#         postData = request.POST
#         first_name = postData.get('firstname')
#         last_name = postData.get('lastname')
#         phone = postData.get('phone')
#         email = postData.get('email')
#         password = postData.get('password')
#         # validation
#         value = {
#             'first_name': first_name,
#             'last_name': last_name,
#             'phone': phone,
#             'email': email
#         }
#         error_message = None

#         customer = Customer(first_name=first_name,
#                             last_name=last_name,
#                             phone=phone,
#                             email=email,
#                             password=password)
#         error_message = self.validateCustomer(customer)

#         if not error_message:
#             print(first_name, last_name, phone, email, password)
#             customer.password = make_password(customer.password)
#             customer.register()
#             return redirect('homepage')
#         else:
#             data = {
#                 'error': error_message,
#                 'values': value
#             }
#             return render(request, 'Signup.html', data)

#     def validateCustomer(self, customer):
#         error_message = None;
#         if (not customer.first_name):
#             error_message = "First Name Required !!"
#         elif len(customer.first_name) < 4:
#             error_message = 'First Name must be 4 char long or more'
#         elif not customer.last_name:
#             error_message = 'Last Name Required'
#         elif len(customer.last_name) < 4:
#             error_message = 'Last Name must be 4 char long or more'
#         elif not customer.phone:
#             error_message = 'Phone Number required'
#         elif len(customer.phone) < 10:
#             error_message = 'Phone Number must be 10 char Long'
#         elif len(customer.password) < 6:
#             error_message = 'Password must be 6 char long'
#         elif len(customer.email) < 5:
#             error_message = 'Email must be 5 char long'
#         elif customer.isExists():
#             error_message = 'Email Address Already Registered..'
#         # saving

#         return error_message

class SignupUser(APIView):
    """
    
    """

    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'status': 403, 'errors': serializer.errors, 'message': 'something went wrong'})

        serializer.save()

        user = User.objects.get(username=serializer.data['username'])
        token_obj, _ = Token.objects.get_or_create(user=user)
        refresh = RefreshToken.for_user(user)
        return Response({'status': 200, 'payload': serializer.data,  'refresh': str(refresh), 'access': str(refresh.access_token), 'token': str(token_obj), 'message': 'user registration success'})


def signupuser(request):
    if request.method=='POST':
        serializer = CustomerSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'status': 403, 'errors': serializer.errors, 'message': 'something went wrong'})

        serializer.save()

        user = User.objects.get(username=serializer.data['username'])
        token_obj, _ = Token.objects.get_or_create(user=user)
        refresh = RefreshToken.for_user(user)
        return Response({'status': 200, 'payload': serializer.data,  'refresh': str(refresh), 'access': str(refresh.access_token), 'token': str(token_obj), 'message': 'user registration success'})
    





@api_view(["POST"])
@permission_classes([AllowAny])
def login_user(request):
    username = request.POST['email']
    print(username)
    password = request.POST['password']
    print(password)
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return Response({'status': 200, })
        # Redirect to a success page.
        ...
    else:
        return Response({'status': 404, })
        # Return an 'invalid login' error message.