
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

from django.core.mail import send_mail
from django.http import HttpResponse

def test_email_view(request):
    send_mail(
        'Temat wiadomości',
        'Treść wiadomości.',
        'therafcio10pl@gmail.com',
        ['wastirtr@gmail.com'],
        fail_silently=False,
    )
    return HttpResponse('Mail został wysłany pomyślnie!')