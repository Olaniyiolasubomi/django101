from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, "assignment/index.html")
def about(request):
    return render(request, "assignment/about.html")
def contact(request):
    return render(request, "assignment/contact.html")
def blog(request):
    return render(request, "assignment/blog.html")