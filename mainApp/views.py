from ast import Return
from contextlib import nullcontext
from django.http import HttpResponse
from django.shortcuts import redirect, render, HttpResponse
from .models import Product, Transaction
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import SignUpForm


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('mainApp')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'login.html'

class CustomLogoutView(LogoutView):
    next_page = '/login/'

@login_required
def index(request):
    product_list = Product.objects.all()
    return render(request, 'index.html', 
    {'products' : product_list})
    #return HttpResponse("Welcome to Inventory Tool")

@login_required
def about(request):
    return render(request, 'about.html')
    #return HttpResponse("A sample Inventory project")

@login_required
def products(request):
    candy_list = candy.objects.all()
    tot = 0
    for candyy in candy_list:
        tot = tot + candyy.quantity
    
    return render(request, 'products.html',
    {'candyyy' : candy_list, 'tot' : tot})
    #return HttpResponse("List of products")

@login_required
def contact(request):
    return render(request, 'contact.html')
    #return HttpResponse("br.kramjit@gmail.com")


@login_required
def sub(request):
    val1 = int(request.POST['val'])
    val2 = request.POST['cname']
    c1 = candy.objects.get(name = val2)
    
    c1.quantity = c1.quantity - val1
    c1.save()

    candy_list = candy.objects.all()
    tot = 0
    for candyy in candy_list:
        tot = tot + candyy.quantity
    
    return render(request, 'purchase.html',
    {'cname1' : val2, 'val': val1, 'tc' :tot})
    
@login_required
def add(request):
    qt = int(request.POST['val'])
    cname = request.POST['cname']
    curl = request.POST['curl']
    
    if(qt > 0):
        c = candy(name=cname, quantity=qt, img=curl)
        c.save()
    
    
    return redirect('/')
    

@login_required
def delete(request):
    
    cname = request.POST['cname']
    c1 = candy.objects.get(name = cname)
    val1 = c1.quantity
    c1.delete()
    candy_list = candy.objects.all()
    tot = 0
    for candyy in candy_list:
        tot = tot + candyy.quantity
    
    return render(request, 'purchase.html',
    {'cname1' : cname, 'val': val1, 'tc' :tot})

@login_required
def assort(request):
    cname1 = request.POST['cname1']
    cname2 = request.POST['cname2']
    cname3 = request.POST['cname3']

    val1 = int(request.POST['val1'])
    val2 = int(request.POST['val2'])
    val3 = int(request.POST['val3'])

    c1 = candy.objects.get(name = cname1)
    c2 = candy.objects.get(name = cname2)
    c3 = candy.objects.get(name = cname3)

    c1.quantity = c1.quantity - val1
    c2.quantity = c2.quantity - val2
    c3.quantity = c3.quantity - val3

    c1.save()
    c2.save()
    c3.save()
    valt = val1 + val2 + val3

    candy_list = candy.objects.all()
    tot = 0
    for candyy in candy_list:
        tot = tot + candyy.quantity

    return render(request, 'purchase.html',
    {'cname1' : cname1 + ',', 'cname2': cname2 + ' and ', 'cname3': cname3, 'val': valt, 'tc':tot})