from django.shortcuts import render, redirect , HttpResponse

# Create your views here.
def Home(request):
    return render(request , "home.html")

def navbar(request):
    return render(request , "navbar.html" )
