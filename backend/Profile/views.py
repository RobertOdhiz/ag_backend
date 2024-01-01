from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import FarmerProfile
from .serializers import FarmerProfileSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication

class FarmerProfileListCreateView(generics.ListCreateAPIView):
    queryset = FarmerProfile.objects.all()
    serializer_class = FarmerProfileSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

class FarmerProfileRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FarmerProfile.objects.all()
    serializer_class = FarmerProfileSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
