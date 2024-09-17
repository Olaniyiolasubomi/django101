from django.urls import path
from .import views
urlpatterns = [
    path("",views.home),
    path("about/",views.about),
    path("contact/",views.contact)
]
# the dot means that the file you are importing is in the same directory

