from django.shortcuts import render
from django.http import HttpResponse
from .models import Tutorial
from .models import Orders
from datetime import datetime
from django.db import models

# Create your views here.
def homepage(request):
    return render(request=request,
    template_name="main/django_index.html",
    context={"orders": Orders.objects.all})
