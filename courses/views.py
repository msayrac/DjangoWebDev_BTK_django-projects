from django.http import HttpResponse, HttpResponseNotFound,HttpResponseRedirect
from django.shortcuts import redirect, render

data ={
    'programlama': "programlama kategorisinde ait kurs listesi",
    'web-gelistirme': "web gelistirme kategorisinde ait kurs listesi",
    'mobil': "mobil kategorisinde ait kurs listesi",
}
# Create your views here.
# eklenen metodlar view olarak adlandırılıyoru

def kurslar(request):
    return HttpResponse("kurs listesi")

def details(request,kurs_adi):
    return HttpResponse(f"{kurs_adi} kursu detay sayfası")

def getCoursesByCategory(request,category_name):
    try:
        category_text = data[category_name]
        return HttpResponse(category_text)
    except:
        return HttpResponseNotFound("yanlış kategori seçimi")

def getCoursesByCategoryId(request,category_id):    
    # return HttpResponseRedirect('/kurs/kategori/programlama')
    category_list = list(data.keys())
    if(category_id > len(category_list)):
       return HttpResponseNotFound("yanlış kategori secimi")
    else:
        redirect_text = category_list[category_id -1]
        return redirect('/kurs/kategori/' +redirect_text) # short cut method instead of HttpResponseRedirect we use redirect

    

