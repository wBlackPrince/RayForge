from django.contrib import admin
from django.urls import path
from django.urls import path, include
from raytracingbasics.views import *

urlpatterns = [
    path('', raytracingbasics_index, name = 'raytracingbasics'),
    path('lesson_1/', raytracingbasics_lesson_1, name = '1.1.lesson'),
    path('lesson_2/', raytracingbasics_lesson_2, name = '1.2.lesson'),
    path('lesson_3/', raytracingbasics_lesson_3, name = '1.3.lesson'),
    path('lesson_4/', raytracingbasics_lesson_4, name = '1.4.lesson'),
    path('lesson_5/', raytracingbasics_lesson_5, name = '1.5.lesson'),
    path('lesson_6/', raytracingbasics_lesson_6, name = '1.6.lesson')
]