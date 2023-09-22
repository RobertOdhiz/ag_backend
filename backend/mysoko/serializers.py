from rest_framework import serializers
from .models import MySoko

class MySokoSerializer(serializers.ModelSerializer):
    user_id = serializers.ReadOnlyField(source='user.id')
    user_first_name = serializers.SerializerMethodField()
    user_last_name = serializers.SerializerMethodField()
    ghala_name = serializers.SerializerMethodField()
    bags_sold = serializers.SerializerMethodField()
    date_sold = serializers.SerializerMethodField()
    commodity_sold = serializers.SerializerMethodField()

    def get_user_first_name(self, obj):
        return obj.user.first_name
    
    def get_bags_sold(self, obj):
        return obj.bags_sold.first().bags_sold
    
    def get_date_sold(self, obj):
        return obj.date_sold.first().date_sold

    def get_user_last_name(self, obj):
        return obj.user.last_name

    def get_ghala_name(self, obj):
        return obj.ghala.first().ghala_name
    
    def get_commodity(self, obj):
        return obj.commodity_stored.first().commodity

    class Meta:
        model = MySoko
        fields = '__all__'
