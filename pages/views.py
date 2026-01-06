from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# eklenen metodlar view olarak adlandırılıyor.

def index(request):
    # return HttpResponse("anasayfa")
    return render(request,'pages/index.html')

def about(request):
    # return HttpResponse("hakkimizda Sayfası")
    return render(request,'pages/about.html')

def contact(request):
    # return HttpResponse("İletisim sayfası")
    return render(request,'pages/contact.html')

