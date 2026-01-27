from django.urls import path
from courses import views

#  http://127.0.0.1:8000/ => anasayfa
#  http://127.0.0.1:8000/home => anasayfa
#  http://127.0.0.1:8000/kurslar => kurs listesi


urlpatterns =[
    path('',views.index),
    path('<slug:slug>',views.details,name='course_details'),
    path('kategori/<str:slug>',views.getCoursesByCategory,name='courses_by_category'),

]

