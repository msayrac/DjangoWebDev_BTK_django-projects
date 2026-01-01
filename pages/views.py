from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# eklenen metodlar view olarak adlandırılıyor.

def home(request):
    return HttpResponse("anasayfa")

def iletisim(request):
    return HttpResponse("İletisim sayfası")

def hakkimizda(request):
    return HttpResponse("hakkimizda Sayfası")