from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# eklenen metodlar view olarak adlandırılıyoru

def kurslar(request):
    return HttpResponse("kurs listesi")

def programlama(request):
    return HttpResponse("programlama kursları")

def mobilUygulamalar(request):
    return HttpResponse("mobil uygulama kursları")

def details(request):
    return HttpResponse("kurs detay sayfası")

