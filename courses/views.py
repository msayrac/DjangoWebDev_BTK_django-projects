from django.http import HttpResponse, HttpResponseNotFound,HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse


data ={
    'programlama': "programlama kategorisinde ait kurs listesi",
    'web-gelistirme': "web gelistirme kategorisinde ait kurs listesi",
    'mobil': "mobil kategorisinde ait kurs listesi",
    '.Net': ".Net kategorisinde ait kurs listesi",
    'R': "R kategorisinde ait kurs listesi",
}
# Create your views here.
# eklenen metodlar view olarak adlandırılıyoru

def index(request):
    category_list = list(data.keys())

    return render(request,'courses/index.html',{
        'categories': category_list
    })

def details(request,kurs_adi):
    return HttpResponse(f"{kurs_adi} kursu detay sayfası")

def getCoursesByCategory(request,category_name):
    try:
        category_text = data[category_name]
        return render(request,'courses/kurslar.html', {
            'category': category_name,
            'category_text': category_text
        })
    except:
        return HttpResponseNotFound("<h1>yanlış kategori seçimi</h1>")

def getCoursesByCategoryId(request,category_id):    
    # return HttpResponseRedirect('/kurs/kategori/programlama')
    category_list = list(data.keys())
    if(category_id > len(category_list)):
       return HttpResponseNotFound("yanlış kategori secimi")
    else:
        category_name = category_list[category_id -1]

        redirect_url = reverse('courses_by_category',args=[category_name])

        return redirect(redirect_url) # short cut method instead of HttpResponseRedirect we use redirect

    

