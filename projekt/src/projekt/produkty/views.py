
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
            'price': product.price
        })

    return render(request, 'home.html', {'attributes': attributes})