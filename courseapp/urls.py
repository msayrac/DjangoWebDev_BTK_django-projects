from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('',include('pages.urls')), 
    path('kurslar/',include('courses.urls')),  
    path('test/',include('courses.urls')), # daha sonra silinecek 
    path('admin/', admin.site.urls),
       
]

# courseapp ana uygulama
# courses
# pages