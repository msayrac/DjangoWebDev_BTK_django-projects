from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# eklenen metodlar view olarak adlandırılıyoru

def kurslar(request):
    return HttpResponse("kurs listesi")

def details(request,kurs_adi):
    return HttpResponse(f"{kurs_adi} kursu detay sayfası")

def getCoursesByCategory(request,category_name):
    text = ""

    if(category_name == 'programlama'):
        text = 'programlama kategorisinde ait kurs listesi'
    elif(category_name == 'web-gelistirme'):
        text = 'web-gelistirme kategorisinde ait kurs listesi'
    else:
        text = 'bilinmeyen kategori'

    return HttpResponse(text)

def getCoursesByCategoryId(request,category_id):
    
    return HttpResponse(category_id)

