from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Blog
from .serializers import BlogSerializer
from .permissions import IsAuthorOrReadOnly
from rest_framework.decorators import action

class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAuthorOrReadOnly]  # Apply the custom permission

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.reads += 1  # Increment reads count
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @action(detail=True, methods=['GET'])
    def read_post(self, request, pk=None):
        post = self.get_object()
        post.increment_reads()
        return Response({'message': 'Read count incremented.'}, status=status.HTTP_200_OK)
