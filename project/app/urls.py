"""docbao_crawler URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django_restful_admin import admin as rest_admin
from app.views import tnv_list

urlpatterns = [
    path('', admin.site.urls),
    path('tinh-nguyen-vien', tnv_list),
    path('api/', rest_admin.site.urls, name="rest_api"),
    path('chaining/', include('smart_selects.urls')),
]
