from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    link = {
        'title':'new page',
        'data':'Welcome to My website 😊'
    }
    return render(request,"index.html",link)