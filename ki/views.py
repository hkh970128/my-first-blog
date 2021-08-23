from django.shortcuts import render
from django.urls.conf import include

from django.utils import timezone

# Create your views here.
def text3(request):
    return render(request, 'text3.html', {})