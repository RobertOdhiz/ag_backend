from django.urls import path
from . import views

urlpatterns = [
    path('blogs/', views.BlogList.as_view(), name='blog-list'),
    path('blogs/<int:pk>/', views.BlogDetail.as_view(), name='blog-detail'),
]
