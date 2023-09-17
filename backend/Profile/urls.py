from django.urls import path
from .views import FarmerProfileListCreateView, FarmerProfileRetrieveUpdateDeleteView

urlpatterns = [
    path('', FarmerProfileListCreateView.as_view(), name='profile-list-create'),
    path('<int:pk>/', FarmerProfileRetrieveUpdateDeleteView.as_view(), name='profile-retrieve-update-delete'),
]
