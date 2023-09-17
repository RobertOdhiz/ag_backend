from django.urls import path
from .views import SokoListCreateView, SokoRetrieveUpdateDeleteView

urlpatterns = [
    path('', SokoListCreateView.as_view(), name='soko-list-create'),
    path('<int:pk>/', SokoRetrieveUpdateDeleteView.as_view(), name='soko-retrieve-update-delete'),
]
