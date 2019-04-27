from django.shortcuts import render
from django.http import HttpResponse
from .models import Restaurant

# Create your views here.
def index(request):
    context = {
        "restaurants": Restaurant.objects.all()
    }
    return render(request, "index.html", context)

def second(request):
    return HttpResponse("Second page")