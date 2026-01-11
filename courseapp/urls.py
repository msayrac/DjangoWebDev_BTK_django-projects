from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('',include('pages.urls')), 
    path('kurs/',include('courses.urls')),  
    path('admin/', admin.site.urls),
       
]

# courseapp ana uygulama
# courses
# pages