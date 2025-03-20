from django.contrib import admin
from django.urls import path
from django.urls import path, include
from raytracingbasics.views import *

urlpatterns = [
    path('', raytracingbasics_index),
    path('lesson_1/', raytracingbasics_lesson_1),
    path('lesson_2/', raytracingbasics_lesson_2),
    path('lesson_3/', raytracingbasics_lesson_3),
    path('lesson_4/', raytracingbasics_lesson_4),
    path('lesson_5/', raytracingbasics_lesson_5),
    path('lesson_6/', raytracingbasics_lesson_6)
]