from django.shortcuts import render, redirect
from .models import *
from django.views import View
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm, CustomerCreationForm
from django.http import JsonResponse


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')

    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def registered(request):
    form = CreateUserForm
    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Account Created')
            return redirect('login')
    return render(request, 'registered.html', {'form': form})


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


class beverages(View):
    def get(self, request):
        beverage = Products.objects.filter(category='BVR')
        return render(request, 'beverages.html', {'beverage': beverage})


# def beverages(request):
# return render(request, 'beverages.html')


def checkout(request):
    return render(request, 'checkout.html')


class gourmet(View):
    def get(self, request):
        gourmets = Products.objects.filter(category='GOUR')
        return render(request, 'gourmet.html', {'gourmets': gourmets})


# def gourmet(request):
# return render(request, 'gourmet.html')


class groceries(View):
    def get(self, request):
        grocerie = Products.objects.filter(category='GR')
        return render(request, 'groceries.html', {'grocerie': grocerie})


# def groceries(request):
# return render(request, 'groceries.html')


class household(View):
    def get(self, request):
        households = Products.objects.filter(category='HH')
        return render(request, 'household.html', {'households': households})


# def household(request):
# return render(request, 'household.html')


def contact(request):
    return render(request, 'contact.html')


def faq(request):
    return render(request, 'faq.html')


def offers(request):
    return render(request, 'offers.html')


class packagedfoods(View):
    def get(self, request):
        packedfood = Products.objects.filter(category='PF')
        return render(request, 'packagedfoods.html', {'packedfood': packedfood})


# def packagedfoods(request):
# return render(request, 'packagedfoods.html')


class personalcare(View):
    def get(self, request):
        personalcares = Products.objects.filter(category='PC')
        return render(request, 'personalcare.html', {'personalcares': personalcares})


# def personalcare(request):
# return render(request, 'personalcare.html')


def products(request):
    return render(request, 'products.html')


class product_detail(View):
    def get(self, request, pk):
        product = Products.objects.get(pk=pk)
        return render(request, 'product detail.html', {'product': product})


# def product_detail(request):
# return render(request, 'product detail.html')


def shortcodes(request):
    return render(request, 'short-codes.html')


def paypage(request):
    return render(request, 'paypage.html')


def updateItem(request):
    return JsonResponse('Item added to cart', safe=False)


# def account(request):
# return render(request, 'account.html')


class account(View):
    def get(self, request):
        form = CustomerCreationForm()
        return render(request, 'account.html', {'form': form})

    def post(self, request):
        form = CustomerCreationForm()
        if form.is_valid():
            usr = request.user
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            mobile = form.cleaned_data['mobile']
            reg = customer(user=usr, name=name, email=email, mobile=mobile)
            reg.save()
            messages.success(request, "Details saved")

        return render(request, 'account.html', {'form': form})


def address(request):
    return render(request, 'address.html')


def history(request):
    return render(request, 'order history.html')

# Create your views here.


# Create your views here.
