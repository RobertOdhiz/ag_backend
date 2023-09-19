from rest_framework import serializers
from .models import MyGhala

class MyGhalaSerializer(serializers.ModelSerializer):
    user_id = serializers.ReadOnlyField(source='user.id')

    class Meta:
        model = MyGhala
        fields = '__all__'
