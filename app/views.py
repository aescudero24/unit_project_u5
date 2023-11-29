from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse

from app.models import ...
from app.forms import ...

# Create your views here.

def home_view(request: HttpRequest) -> HttpResponse:
    return render(request, "home.html")
