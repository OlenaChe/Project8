from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('results/', views.results, name="results"),
    path('<int:product_id>/', views.descriptions, name="descriptions"),
    path('products/', views.products, name="products"),
    path('mentions/', views.mentions, name="mentions"),
]
