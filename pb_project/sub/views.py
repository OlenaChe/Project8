from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

#from .models import ALBUMS


def index(request):
    return render(request, 'sub/index.html')

def accounts(request):
    return render(request, 'registration/login.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username, password = password)
            login(request, user)
            return redirect('index')

    else:
        form = UserCreationForm()
    context = {'form':form}
    return render(request, 'registration/register.html', context)

def result(request):
    return render(request, 'sub/result.html')

def products(request):
    return render(request, 'sub/products.html')

def mentions(request):
    return render(request, 'sub/mentions.html')

#---------------------------
def detail(request, album_id):
    id = int(album_id) # make sure we have an integer.
    album = ALBUMS[id] # get the album with its id.
    artists = " ".join([artist['name'] for artist in album['artists']]) # grab artists name and create a string out of it.
    message = "Le nom de l'album est {}. Il a été écrit par {}".format(album['name'], artists)
    return HttpResponse(message)

def search(request):
    query = request.GET.get('query')
    if not query:
        message = "Aucun artiste n'est demandé"
    else:
        albums = [
            album for album in ALBUMS
            if query in " ".join(artist['name'] for artist in album['artists'])
        ]

        if len(albums) == 0:
            message = "Misère de misère, nous n'avons trouvé aucun résultat !"
        else:
            albums = ["<li>{}</li>".format(album['name']) for album in albums]
            message = """
                Nous avons trouvé les albums correspondant à votre requête ! Les voici :
                <ul>
                    {}
                </ul>
            """.format("</li><li>".join(albums))

    return HttpResponse(message)