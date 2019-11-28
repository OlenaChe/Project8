from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from .forms import RegisterForm

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

def products(request):
    return render(request, 'sub/products.html')

def mentions(request):
    return render(request, 'sub/mentions.html')

def result(request):
    return render(request, 'sub/result.html')
    