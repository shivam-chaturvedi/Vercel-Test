from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post/', views.create_blog, name='blog_post'),
    
    path('clear/', views.clear),
]
