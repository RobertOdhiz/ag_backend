from rest_framework import generics, status
from .models import Soko
from .serializers import SokoSerializer
from rest_framework.response import Response
from datetime import timedelta
from django.utils import timezone


class SokoListCreateView(generics.ListCreateAPIView):
    queryset = Soko.objects.all()
    serializer_class = SokoSerializer

class SokoRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Soko.objects.all()
    serializer_class = SokoSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.user == request.user and instance.created_at >= timezone.now() - timedelta(days=1):
            return super().update(request, *args, **kwargs)
        return Response({"message": "Update not allowed."}, status=status.HTTP_403_FORBIDDEN)