from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blog_detail/<slug:blog_slug>/', views.blog_detail, name='blog_detail'),
    path('portfolio_detail/', views.portfolio_detail, name='portfolio_detail'),
]