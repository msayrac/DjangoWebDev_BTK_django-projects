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

def details(request,kurs_id):

    # try:
    #     course = Course.objects.get(pk=kurs_id)
    # except:
    #     raise Http404()

    course = get_object_or_404(Course,pk=kurs_id)
    
    context = {
            'course':course        
        }
    return render(request,'courses/details.html',context)
    
    

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

    

