from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# eklenen metodlar view olarak adlandırılıyoru

def kurslar(request):
    return HttpResponse("kurs listesi")

def details(request):
    return HttpResponse("kurs detay sayfası")

def getCoursesByCategory(request,category):
    text = ""

    if(category == 'programlama'):
        text = 'programlama'
    elif(category == 'web-gelistirme'):
        text = 'web-gelistirme'
    else:
        text = 'bilinmeyen kategori'

    return HttpResponse(f"{text} kategorisinde ait kurs listesi")

 