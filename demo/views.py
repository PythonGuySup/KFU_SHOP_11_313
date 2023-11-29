from django.shortcuts import render
from django.shortcuts import HttpResponse, render
# Create your views here.
def home_page(request):
    return render(request, "home_page.html")

def shop_page(request):
    return HttpResponse("<reh1>Здесь пока пусто<h1>")