from rest_framework import serializers
from .models import Ghala, Rating

class GhalaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ghala
        fields = '__all__'

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'
        
