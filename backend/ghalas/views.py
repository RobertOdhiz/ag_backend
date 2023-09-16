from rest_framework import generics
from .models import Ghala, Rating
from .serializers import GhalaSerializer, RatingSerializer


class GhalaListCreateView(generics.ListCreateAPIView):
    queryset = Ghala.objects.all()
    serializer_class = GhalaSerializer

class GhalaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ghala.objects.all()
    serializer_class = GhalaSerializer

class RatingListCreateView(generics.ListCreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

class RatingRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
