from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    # return HttpResponse("God is great and you know it")
    return render(request, "first_django/index.html")
def about(request):
    # return HttpResponse("He is always with me")
    return render(request, "first_django/about.html")
def contact(request):
    # return HttpResponse("God is my guiding light")
    return render(request, "first_django/contact.html")