from django.shortcuts import render, redirect , HttpResponse

# Create your views here.
def Home(request):
    return render(request , "home.html")

def navbar(request):
    return render(request , "navbar.html" )

def about(request):
    return render(request , "about.html" )

def skill(request):
    return render(request , "skill.html" )

def contact(request):
    return render(request , "contact.html" )