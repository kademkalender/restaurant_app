from rest_framework import serializers
from .models import Restaurants

class RestaurantsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurants
        fields = ['id', 'res_name', 'res_category', 'address', 'publish_date', 'image_url']