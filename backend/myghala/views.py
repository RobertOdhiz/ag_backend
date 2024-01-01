from rest_framework import generics
from .models import MyGhala
from .serializers import MyGhalaSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication

class MyGhalaListCreateView(generics.ListCreateAPIView):
    serializer_class = MyGhalaSerializer

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return MyGhala.objects.filter(user=self.request.user)
        else:
            return MyGhala.objects.none()

class MyGhalaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MyGhalaSerializer

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return MyGhala.objects.filter(user=self.request.user)
        else:
            return MyGhala.objects.none()

