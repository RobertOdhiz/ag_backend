from rest_framework import serializers
from .models import MyGhala

class MyGhalaSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyGhala
        fields = '__all__'
