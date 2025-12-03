from django.shortcuts import render 
from django.http import HttpResponse

def about(request):
    # return HttpResponse("This is about view")
    return render(request,"about.html")
def home(request):
    # return HttpResponse("This is home view")
    return render(request,"home.html")
def contact(request):
    # return HttpResponse("This is contactt view")
    return render(request,"contact.html")
def login(request):
    # return HttpResponse("This is login view")
    return render(request,"login.html")
def register(request):
    # return HttpResponse("This is register view")
    return render(request,"register.html")

