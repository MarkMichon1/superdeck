from django.shortcuts import render

def home(request):
    return render(request, 'frontend/home.html')


def about(request):
    return render(request, 'frontend/about.html')


def articles(request):
    return render(request, 'frontend/articles.html')


def contact(request):
    return render(request, 'frontend/contact.html')


def services(request):
    return render(request, 'frontend/services.html')

# to do:  testimonials, previous work