"""
URL configuration for project project.

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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('lekce2/', include('lekce2.urls')),
    path('ukol/', include('ukol.urls')),
    path('lekce3/', include('lekce3.urls')),
    path('ukol2/', include('ukol2.urls')),
    path('lekce4/', include('lekce4.urls')),
    path('ukol3/', include('ukol3.urls')),
    path('lekce5/', include('lekce5.urls')),
]
