from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('wishlist/', views.wishlist_list, name='wishlist-list'),
    path('wishlist/<slug:slug>/', views.toggle_wishlist, name='toggle-wishlist'),
    path('like/<slug:slug>/', views.toggle_like, name='toggle-like'),
]