from rest_framework import generics
from rest_framework import viewsets
from .models import Ghala, Rating
from .serializers import GhalaSerializer, RatingSerializer
from django.db.models import Q
from rest_framework.permissions import IsAuthenticated


class GhalaListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Ghala.objects.all()
    serializer_class = GhalaSerializer

class GhalaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Ghala.objects.all()
    serializer_class = GhalaSerializer

class RatingListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

class RatingRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

class GhalaSearchViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Ghala.objects.all()
    serializer_class = GhalaSerializer

    def get_queryset(self):
        query_params = self.request.query_params
        search_query = query_params.get('search', '')

        # Split the search query into individual characters
        characters = [char for char in search_query]

        # Initialize an empty Q object to build the OR condition
        q_object = Q()

        # Build the OR condition by applying 'icontains' filter for each character
        for char in characters:
            q_object |= Q(ghala_name__icontains=char) | Q(description__icontains=char)

        # Apply the OR condition to the queryset
        queryset = Ghala.objects.filter(q_object)

        return queryset