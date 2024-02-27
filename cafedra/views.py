from django.shortcuts import render, HttpResponse
from django.core.exceptions import ObjectDoesNotExist
import random

from .models import FilePage, InfoPage, EmployeePage, MainPage

def main_page(req):

    main = MainPage.objects.all()

    for main_page in main:
        title_university = main_page.title_university
        name = main_page.name
        position = main_page.position
        short_info = main_page.short_info
        summary = main_page.summary
        address = main_page.address
        phone_number = main_page.phone_number
        email = main_page.email
        photo_deportament = main_page.photo_deportament
        photo = main_page.photo


    context = {
        'main_page': main_page
    }


    return render(req, 'main.html', context)

def cafedra_page(req):
    regulars = list(InfoPage.objects.all())
    files = list(FilePage.objects.all())
    employes = list(EmployeePage.objects.all())

    combined = regulars + files + employes

    context = {
        'pages': combined
    }

    return render(req, 'cafedra.html', context)

def regular(req, slug):
    try:
        page = InfoPage.objects.get(slug=slug)
        context = {
            'page': page,
        }
        return render(req, 'first-slide.html', context)
    except ObjectDoesNotExist:
        return HttpResponse("404")

def employee_page(req, slug):
    try:
        page = EmployeePage.objects.get(slug=slug)
        context = {
            'page': page,
        }
        return render(req, 'employes.html', context)
    except ObjectDoesNotExist:
        return HttpResponse("404")

def index_page(req, slug):
    try:
        page = FilePage.objects.get(slug=slug)
        context = {
            'page': page,
        }
        return render(req, 'index.html', context)
    except ObjectDoesNotExist:
        return HttpResponse("404")
    


