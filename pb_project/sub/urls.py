from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('results/', views.results, name="results"),
    path('substitutes/<int:product_id>/', views.substitutes, name="substitutes"),
    path('descriptions/<int:product_id>/', views.descriptions, name="descriptions"),
    path('products/', views.products, name="products"),
    path('mentions/', views.mentions, name="mentions"),
]
