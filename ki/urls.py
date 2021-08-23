from django.urls import path
from . import views

urlpatterns = [
    path('text2/text3/', views.text3, name='text3'),
    ]