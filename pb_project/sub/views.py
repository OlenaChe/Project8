from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

#from .forms import ContactForm, ParagraphErrorList

from .forms import RegisterForm

#from .models import ALBUMS


def index(request):
    return render(request, 'sub/index.html')

def logout(request):
    logout(request)
    return redirect("registration/login.html")
    # Redirect to a success page.
"""
def accounts(request):
    return render(request, 'registration/login.html')

def logout(request):
    return render(request, 'logout.html')
"""
def register(request):
    if request.method == 'POST':
        #form = UserCreationForm(request.POST)
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            user = authenticate(username = username, password = password, email = email)
            #login(request, user)
            #return redirect('index')
            if user:
                if user.is_active:
                    auth_login(request, user)
                    return HttpResponseRedirect(request.GET.get('next',
                                                settings.LOGIN_REDIRECT_URL))

    else:
        #form = UserCreationForm()
        form = RegisterForm()
    context = {'form':form}
    return render(request, 'registration/register.html', context)
"""
def register(request, context):
    
    if request.method == 'POST':
        form = ContactForm(request.POST, error_class=ParagraphErrorList)
        context = {'form':form}
        if form.is_valid():
            email = form.cleaned_data['email']
            name = form.cleaned_data['name']

            contact = Contact.objects.filter(email=email)
            if not contact.exists():
                # If a contact is not registered, create a new one.
                contact = Contact.objects.create(
                    email=email,
                    name=name
                )
            else:
                contact = contact.first()
            
            return render(request, 'sub/index.html', context)
        else:
            # Form data doesn't match the expected format.
            # Add errors to the template.
            context['errors'] = form.errors.items()
    else:
        form = ContactForm()
    context = {'form':form}
    return render(request, 'registration/register.html', context)
"""
def result(request):
    return render(request, 'sub/result.html')

def products(request):
    return render(request, 'sub/products.html')

def mentions(request):
    return render(request, 'sub/mentions.html')