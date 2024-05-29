from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10000, decimal_places=2)
    image = models.ImageField(upload_to='produkty/product_images/', blank=True)

    
    