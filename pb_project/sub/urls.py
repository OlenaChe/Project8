from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('products/', views.products, name="products"),
    path('register/', views.register, name="register"),
    path('mentions/', views.mentions, name="mentions"),
]
