from django.db import models

# Create your models here.
class Restaurants(models.Model):
    id = models.AutoField(primary_key=True) 
    res_name = models.CharField(max_length=100) 
    res_category = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    publish_date = models.DateField()
    image_url = models.URLField(blank=True, null=True)
    
def __str__(self):
    return self.res_name
