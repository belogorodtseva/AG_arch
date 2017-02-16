from django.shortcuts import render

def index(request):
    return render(request, 'home.html')

def architecture(request):
    return render(request, 'architecture.html')

def design(request):
    return render(request, 'design.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    return render(request, 'contact.html')
