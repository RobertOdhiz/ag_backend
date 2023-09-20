from rest_framework import generics
from .models import MySoko
from .serializers import MySokoSerializer

class MySokoListCreateView(generics.ListCreateAPIView):
    serializer_class = MySokoSerializer

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return MySoko.objects.filter(user=self.request.user)
        else:
            return MySoko.objects.none()

class MySokoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MySokoSerializer

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return MySoko.objects.filter(user=self.request.user)
        else:
            return MySoko.objects.none()
