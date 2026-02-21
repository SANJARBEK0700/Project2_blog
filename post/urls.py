from _pyrepl.commands import home

from django.urls import path
from . import views

app_name = 'post'

urlpatterns = [
    path('', views.PostListView.as_view(), name='post-list'),
    path('create/', views.PostCreateView.as_view(), name='post-create'),
    path('<slug:slug>/', views.PostDetailView.as_view(), name='post-detail'),
    path('<slug:slug>/update/', views.PostUpdateView.as_view(), name='post-update'),
    path('<slug:slug>/delete/', views.PostDeleteView.as_view(), name='post-delete'),
    path("home/", views.home_view, name="home"),
]