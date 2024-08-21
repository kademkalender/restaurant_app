"""
URL configuration for restaurant_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from restaurants.views import restaurant_list, RestaurantsViewSet,restaurant_create,restaurant_delete,restaurant_update
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'restaurants', RestaurantsViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('restaurants/',restaurant_list, name='restaurant-list'),
    path('api/restaurants/create/', restaurant_create, name='restaurant-create'),
    path('api/restaurants/<int:id>/', restaurant_update, name='restaurant-update'),
    path('api/restaurants/<int:id>/delete/', restaurant_delete, name='restaurant-delete'),
]
