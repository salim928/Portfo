from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact, Blogs

# Create your views here.

def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")



def contact(request):
    if request.method=="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phoneno = request.POST.get('num')
        desc = request.POST.get('desc')

        query = Contact(name=name, email=email,phonenumber=phoneno,description=desc)
        query.save()
        messages.success(request, "Thanks for conatcting me. I'll get back to you soon!")
        return redirect('/contact')
       

    return render(request, "contact.html")

def handleblog(request):
    posts = Blogs.objects.all()
    context = {"posts":posts}

    return render(request, "handleblogs.html", context)
