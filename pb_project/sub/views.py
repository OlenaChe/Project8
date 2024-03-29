from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
#from django.core.paginator import Paginator

from .forms import RegisterForm


from .models import Contact, Product, Category, Favorite

import requests

def index(request):
    return render(request, 'sub/index.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            user = authenticate(username = username, password = password, email = email)
            login(request, user)
            return redirect('index')
    else:
        form = RegisterForm()
    context = {'form':form}
    return render(request, 'registration/register.html', context)

def results(request):
    query = request.GET.get('query')
    if len(str(query)) < 3:
        return render(request, 'sub/results.html')  
    else:
        products = Product.objects.filter(name__icontains=query)
        
        context = {
                'products': products,    
            }
        return render(request, 'sub/results.html', context)

def substitutes(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    product_name = product.name
    category = product.category
    product_score = product.score
    sub = Product.objects.filter(category=product.category).filter(score__lt=product_score)
    context = {
            'sub': sub,
            'product_name': product.name,    
        }
    return render(request, 'sub/substitutes.html', context)  

@login_required
def get_favorite(request, product_id):
    favorite = get_object_or_404(Product, pk=product_id)
    contact = Contact.objects.get(user_id=request.user)
    context = {
        'favorite': favorite,
        'contact': contact,    
    }
    obj, created = Favorite.objects.update_or_create(favorite = favorite, contact = contact)
    return render(request, 'sub/add_favorite.html', context)  

@login_required
def products(request):
    favorite = Favorite.objects.all()
    contact = Contact.objects.get(user_id=request.user)
    context = {
        'favorite': favorite,
        'contact': contact,    
    }
    return render(request, 'sub/products.html', context)
    
def mentions(request):
    return render(request, 'sub/mentions.html')

def descriptions(request, product_id):
    product = Product.objects.get(pk=product_id)
    context = {
        'product_name': product.name,
        'product_description': product.description,
        'product_score': product.score,
        'product_url': product.url,
        'product_img': product.img,
        'product_url': product.url,
        'product_nutrition': product.nutrition,

    }
    return render(request, 'sub/descriptions.html', context)