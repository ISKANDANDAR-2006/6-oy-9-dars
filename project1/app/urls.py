from django.urls import path
from . import views

urlpatterns = [
    path('add-course/', views.add_course, name='add_course'),
    path('add-lesson/', views.add_lesson, name='add_lesson'),
    path('add-tur/', views.add_tur, name='add_tur'),
    path('add-gul/', views.add_gul, name='add_gul'),
]
