from django.shortcuts import render,redirect

def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')