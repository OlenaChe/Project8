from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator

from .forms import RegisterForm


from .models import Contact, Product, Category, Substitute

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
"""
def results(request):
    query = request.GET.get('query')
    if len(str(query)) <= 3:
        context = {
            'products': products
        }
        message = "Vous devez écrire le nom du produit"
    else:
        # title contains the query is and query is not sensitive to case.
        products = Product.objects.filter(name__icontains=query)

        if not products.exists():
            products = Product.objects.filter(description__icontains=query)

        if not products.exists():
            message = "Désolé, nous n'avons trouvé aucun produit !"
        else:
            products = ["<li>{}</li>".format([product.name, product.score]) for product in products]
            message = "
                Nous avons trouvé les produits correspondant à votre requête ! Les voici :
                <ul>{}</ul>
            ".format("</li><li>".join(products))
        context = {
            'products': products
        }
        return render(request, 'sub/results.html', context)
        #return HttpResponse(message)
    #return HttpResponse(message)
    context = {
        'products': products
    }
    return render(request, 'sub/results.html', context)
"""
def results(request):
    query = request.GET.get('query')
    if len(query) < 3:
        return render(request, 'sub/results.html')  
    else:
        products = Product.objects.filter(name__icontains=query)
        context = {
                'products': products,    
            }
        return render(request, 'sub/results.html', context)

def products(request):
    return render(request, 'sub/products.html')
    
def mentions(request):
    return render(request, 'sub/mentions.html')

def descriptions(request, product_id):
    product = Product.objects.get(pk=product_id)
    #product_name = " ".join(products)
    context = {
        'product_name': product.name,
        'product_score': product.score,
        'product_url': product.url,
        'product_img': product.img
    }
    return render(request, 'sub/descriptions.html', context)