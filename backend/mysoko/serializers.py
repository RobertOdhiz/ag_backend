from rest_framework import serializers
from .models import MySoko

class MySokoSerializer(serializers.ModelSerializer):
    user_first_name = serializers.ReadOnlyField(source='user.first_name')
    user_last_name = serializers.ReadOnlyField(source='user.last_name')
    ghala_name = serializers.ReadOnlyField(source='my_ghala.ghala.ghala_name')
    date_sold = serializers.ReadOnlyField(source='date_sold.date_sold')
    commodity_sold = serializers.ReadOnlyField(source='commodity_sold.name')

    class Meta:
        model = MySoko
        fields = '__all__'
