from django.urls import path
from .views import (GhalaListCreateView, 
                    GhalaRetrieveUpdateDestroyView, 
                    RatingListCreateView, 
                    RatingRetrieveUpdateDestroyView
                    )

urlpatterns = [
    path('', GhalaListCreateView.as_view(), name='ghala-list-create'),
    path('<int:pk>/', GhalaRetrieveUpdateDestroyView.as_view(), name='ghala-detail'),
    path('ratings/', RatingListCreateView.as_view(), name='rating-list-create'),
    path('ratings/<int:pk>/', RatingRetrieveUpdateDestroyView.as_view(), name='rating-detail'),
]