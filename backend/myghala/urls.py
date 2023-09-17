from django.urls import path
from . import views

urlpatterns = [
    path('', views.MyGhalaListCreateView.as_view(), name='myghala-list-create'),
    path('<int:pk>/', views.MyGhalaRetrieveUpdateDestroyView.as_view(), name='myghala-detail'),
]
