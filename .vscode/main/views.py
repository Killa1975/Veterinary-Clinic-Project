from django.shortcuts import render
import re
from django.utils.timezone import datetime
from django.http import HttpResponse

def main_page(request):
    print(request.build_absolute_uri()) #optional
    return render(
        request,
        'page/main_page.html'
    )

def home(request):
    return HttpResponse("Hello, Django!")
