from rest_framework import serializers
from .models import Blog

class BlogSerializer(serializers.ModelSerializer):
    author_first_name = serializers.ReadOnlyField(source='author.first_name')
    author_last_name = serializers.ReadOnlyField(source='author.last_name')
    author_avatar = serializers.ReadOnlyField(source='FarmerProfile.author.avatar')

    class Meta:
        model = Blog
        fields = '__all__'
