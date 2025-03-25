from django.http import HttpResponse
from django.shortcuts import render


def index(request): #HttpRequest
    return render(request, 'raytracingbasics/index.html')

def raytracingbasics_index(request): #HttpRequest
    return render(request, 'raytracingbasics/raytracing_basics_index.html')

def customsrp_index(request):
    return render(request, 'raytracingbasics/customsrp_index.html')

def rendering_index(request):
    return render(request, 'raytracingbasics/rendering_index.html')

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