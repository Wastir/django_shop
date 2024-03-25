"""
URL configuration for projekt project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path

from strony.views import home_view, about_view
from produkty.views import products_view, product_detail
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', products_view, name='home'),
    path('about/', about_view, name='about'),
    path('admin/', admin.site.urls),
    path('<int:id>', product_detail, name='product_detail'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
