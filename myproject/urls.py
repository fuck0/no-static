
from django.contrib import admin
from django.urls import path

from sunapp import views

urlpatterns = [
    path('Boom/', views.index),
    path('admin/', admin.site.urls),
]
