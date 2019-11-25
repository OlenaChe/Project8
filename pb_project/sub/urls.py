from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('products/', views.products, name="products"),
    path('register/', views.register, name="register"),
    path('mentions/', views.mentions, name="mentions"),
    
    #path('result/', views.result, name="result"),
    #path('', views.listing, name="listing"),
    #path('<int:album_id>/', views.detail, name='detail'),   
    #path('search/', views.search, name="search"),  
]
