from django.shortcuts import render
from django.urls.conf import include

from django.utils import timezone

# Create your views here.
def text4(request):
    return render(request, 'text4.html', {})