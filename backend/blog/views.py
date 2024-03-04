from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.urls import reverse
from blog.models import Blog
from .serializers import BlogSerializer
from rest_framework.permissions import SAFE_METHODS, BasePermission

class BlogUserWritePermission(BasePermission):
    message = 'Editing blogs is restricted to the author only.'

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user

class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [BlogUserWritePermission]

    @action(detail=False, methods=['get'], url_path='blog-api')
    def blog_api_routes(self, request):
        """
        Custom action to list all available paths for Blog operations.
        """
        paths = {
            'Create Blog': 'blog-create',
            'List All Blogs': 'blog-list',
            'Retrieve Blog': 'blog-retrieve',
            'Update Blog': 'blog-update',
            'Delete Blog': 'blog=delete'
        }
        return Response(paths)

    @action(detail=False, methods=['post'], url_path='blog-create')
    def blog_create(self, request):
        """
        Custom action to create a new Blog instance.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(author=request.user)  
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['put'], url_path='blog-update')
    def blog_update(self, request, pk=None):
        """
        Custom action to update an existing Blog instance.
        """
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(author=request.user)  
        return Response(serializer.data)

    @action(detail=True, methods=['delete'], url_path='blog-delete')
    def blog_delete(self, request, pk=None):
        """
        Custom action to delete an existing Blog instance.
        """
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'message': f'Blog with id={pk} deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

    @action(detail=False, methods=['get'], url_path='blog-list')
    def blog_list(self, request):
        """
        Custom action to list all Blog instances.
        """
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'], url_path='blog-retrieve')
    def blog_retrieve(self, request, pk=None):
        """
        Custom action to retrieve a specific Blog instance.
        """
        instance = self.get_object()
        instance.reads += 1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
