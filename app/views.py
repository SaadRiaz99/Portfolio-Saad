from django.shortcuts import render, redirect , HttpResponse
from django.contrib import messages
from django.db import OperationalError
from .models import Contact

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
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message_text = request.POST.get('message')
        if not name or not email or not message_text:
            messages.error(request, 'Please fill in all fields.')
            return redirect('contact')
        try:
            Contact.objects.create(name=name, email=email, message=message_text)
        except OperationalError:
            messages.error(request, 'Database table missing. Run migrations (see instructions).')
            return redirect('contact')
        messages.success(request, 'Thanks — your message has been received.')
        return redirect('contact')
    return render(request , "contact.html" )