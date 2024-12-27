from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name='store'),
    path('cart/', views.car, name='cart'),
    path('checkout/', views.checkout, name="checkout")
]
