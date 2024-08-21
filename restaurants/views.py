from django.shortcuts import render,get_object_or_404
from .models import Restaurants
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status 
from django.http import JsonResponse
from .serializers import RestaurantsSerializer
from rest_framework import viewsets
import json

# Create your views here.
class RestaurantsViewSet(viewsets.ModelViewSet):
    queryset = Restaurants.objects.all()
    serializer_class = RestaurantsSerializer

def restaurant_list(request):
    restaurants = Restaurants.objects.all()
    data = {
            'restaurants': [{
                'id': restaurant.id,
                'res_name': restaurant.res_name,
                'res_category': restaurant.res_category,
                'address': restaurant.address,
                'image_url': restaurant.image.url if restaurant.image else None,
                'publish_date': restaurant.publish_date
            }for restaurant in restaurants]
    }
    return JsonResponse(data)

@api_view(['GET'])
def restaurant_list(request):
    """
    List all restaurants or create a new restaurant.
    """
    if request.method == 'GET':
        restaurants = Restaurants.objects.all()
        serializer = RestaurantsSerializer(restaurants, many=True)
        return Response(serializer.data)

@api_view(['POST'])
def restaurant_create(request):
    """
    Create a new restaurant.
    """
    if request.method == 'POST':
        serializer = RestaurantsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def restaurant_update(request, id):
    """
    Update an existing restaurant.
    """
    restaurant = get_object_or_404(Restaurants, pk=id)
    serializer = RestaurantsSerializer(restaurant, data=request.data, partial=True)
    if serializer.is_valid():
        # Gelen verileri model üzerinde güncelle
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def restaurant_delete(request, id):
    """
    Delete an existing restaurant.
    """
    restaurant = get_object_or_404(Restaurants, pk=id)
    restaurant.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)