from rest_framework import generics
from .models import MyGhala
from .serializers import MyGhalaSerializer  

class MyGhalaListCreateView(generics.ListCreateAPIView):
    queryset = MyGhala.objects.all()
    serializer_class = MyGhalaSerializer

class MyGhalaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MyGhala.objects.all()
    serializer_class = MyGhalaSerializer
