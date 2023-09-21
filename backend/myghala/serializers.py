from rest_framework import serializers
from .models import MyGhala

class MyGhalaSerializer(serializers.ModelSerializer):
    user_id = serializers.ReadOnlyField(source='user.id')
    user_first_name = serializers.SerializerMethodField()
    user_last_name = serializers.SerializerMethodField()
    ghala_name = serializers.SerializerMethodField()
    commodity_name = serializers.SerializerMethodField()
    commodity_price = serializers.SerializerMethodField()

    def get_commodity_price(self, obj):
        return obj.commodity_stored.first().price

    def get_user_first_name(self, obj):
        return obj.user.first_name

    def get_user_last_name(self, obj):
        return obj.user.last_name

    def get_ghala_name(self, obj):
        return obj.ghala.first().ghala_name
    
    def get_commodity_name(self, obj):
        return obj.commodity_stored.first().commodity

    class Meta:
        model = MyGhala
        fields = '__all__'
