from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request): #HttpRequest
    return HttpResponse('Уроки по математике и программированию')

def raytracingbasics_index(request): #HttpRequest
    return HttpResponse('Уроки по ray tracing')

def raytracingbasics_lesson_1(request): #HttpRequest
    return render(request, 'raytracingbasics/1_lesson.html')

def raytracingbasics_lesson_2(request): #HttpRequest
    return render(request, 'raytracingbasics/2_lesson.html')

def raytracingbasics_lesson_3(request): #HttpRequest
    return render(request, 'raytracingbasics/3_lesson.html')

def raytracingbasics_lesson_4(request): #HttpRequest
    return render(request, 'raytracingbasics/4_lesson.html')

def raytracingbasics_lesson_5(request): #HttpRequest
    return render(request, 'raytracingbasics/5_lesson.html')

def raytracingbasics_lesson_6(request): #HttpRequest
    return render(request, 'raytracingbasics/6_lesson.html')