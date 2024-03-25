
from django.shortcuts import render

from .models import Product
# Create your views here.
def products_view(request):
    products = Product.objects.all()
    attributes = []
    for product in products:
        attributes.append({
            'id': product.id,
            'name': product.name,
            'description': product.description,
            'price': product.price,
            'image' : product.image,
        })

    return render(request, 'home.html', {'attributes': attributes})

# Product details
def product_detail(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'product_detail.html', {'product': product})