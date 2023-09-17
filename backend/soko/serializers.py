from rest_framework import serializers
from .models import Soko

class SokoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Soko
        fields = "__all__"