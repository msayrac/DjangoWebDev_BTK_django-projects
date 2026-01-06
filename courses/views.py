from django.http import HttpResponse, HttpResponseNotFound,HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse


data ={
    'programlama': "programlama kategorisinde ait kurs listesi",
    'web-gelistirme': "web gelistirme kategorisinde ait kurs listesi",
    'mobil': "mobil kategorisinde ait kurs listesi",
}
# Create your views here.
# eklenen metodlar view olarak adlandırılıyoru

def index(request):
    return render(request,'courses/index.html')

def kurslar(request):
    list_items = ""
    category_list = list(data.keys())

    for category in category_list:
        redirect_url = reverse('courses_by_category',args=[category])
        list_items += f"<li><a href='{redirect_url}'>{category}</a></li>"
    
    html = f"<h1>Kurslar listesi</h1><br><ul>{list_items}</ul>"

    return HttpResponse(html)

def details(request,kurs_adi):
    return HttpResponse(f"{kurs_adi} kursu detay sayfası")

def getCoursesByCategory(request,category_name):
    try:
        category_text = data[category_name]
        return HttpResponse(category_text)
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

    

