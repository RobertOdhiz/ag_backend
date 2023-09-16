from django.urls import path
from . import views

urlpatterns = [
    path('myghalas/', views.MyGhalaListCreateView.as_view(), name='myghala-list-create'),
    path('myghalas/<int:pk>/', views.MyGhalaRetrieveUpdateDestroyView.as_view(), name='myghala-detail'),
]
