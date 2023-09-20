from django.urls import path
from . import views

urlpatterns = [
    path('', views.MySokoListCreateView.as_view(), name='mysoko-list-create'),
    path('<int:pk>/', views.MySokoRetrieveUpdateDestroyView.as_view(), name='mysoko-detail'),
]