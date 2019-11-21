from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('account/', views.account, name="account"),
    path('result/', views.result, name="result"),
    path('products/', views.products, name="products"),
    #path('', views.listing, name="listing"),
    #path('<int:album_id>/', views.detail, name='detail'),   
    #path('search/', views.search, name="search"),  
]
