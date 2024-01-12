"""
URL configuration for project25 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from app.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('htmlform/',htmlform,name='htmlform'),
    path('create_Topic/',create_Topic,name='create_Topic'),
    path('create_Webpage/',create_Webpage,name='create_Webpage'),
    path('create_Accessrecord/',create_Accessrecord,name='create_Accessrecord'),
    path('display_multiple_Webpage/',display_multiple_Webpage,name='display_multiple_Webpage'),
    path('checkbox/',checkbox,name='checkbox'),
    path('display_multiple_Accessrecord/',display_multiple_Accessrecord,name='display_multiple_Accessrecord'),
    path('checkbox_Accessrecord/',checkbox_Accessrecord,name='checkbox_Accessrecord'),
]

