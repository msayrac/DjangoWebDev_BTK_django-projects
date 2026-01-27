from datetime import date,datetime
from django.http import Http404, HttpResponseNotFound
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from courses.models import Course,Category



db = {
    'courses' :[
        {"title": "javascript kursu",
         "description": "javascript kurs aciklaması",
         "imageUrl": "1.jpg",
         "slug":"javascript-kursu",
         "date": datetime.now(),
         "isActive": True,
         "isUpdated": False     
         },         

         {"title": "python kursu",
         "description": "python kurs aciklaması",
         "imageUrl": "2.jpg",
         "slug":"python-kursu",
         "date": date(2025,12,10),
         "isActive": False,
         "isUpdated": False              
         },

         {"title": "web gelistirme kursu",
         "description": "web gelistirme kurs aciklaması",
         "imageUrl": "3.jpg",
         "slug":"web-gelistirme",
         "date": date(2026,1,15),
         "isActive": True,
         "isUpdated": True              
         },
    ],
    "categories": [
        {"id": 1, "name" : "programlama", "slug":"programlama"},
        {"id": 2, "name" : "web gelistirme", "slug":"web-gelistirme"},
        {"id": 3, "name" : "mobil uygulamalar", "slug":"mobil-uygulamalar"},
    ]
}


def index(request):
    # list comprehension   
    kurslar = Course.objects.filter(isActive=1)

    kategoriler = Category.objects.all()

    return render(request,'courses/index.html',{
        'categories': kategoriler,
        'courses':kurslar
    })

def details(request,slug):

    course = get_object_or_404(Course,slug=slug)
    
    context = {
            'course':course        
        }
    return render(request,'courses/details.html',context)
    
    

def getCoursesByCategory(request,slug):
    kurslar = Course.objects.filter(category__slug = slug, isActive = True)
    kategoriler = Category.objects.all()

    return render(request, 'courses/index.html', {
        'categories': kategoriler,
        'courses':kurslar,
        'seciliKategori': slug
    })
   


    

