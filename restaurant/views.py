from django.shortcuts import render


def home(request):
    return render(request, 'restaurant/home.html')


def menu(request):
    return render(request, 'restaurant/menu.html')


def about(request):
    return render(request, 'restaurant/about.html')


def contact(request):
    return render(request, 'restaurant/contact.html')