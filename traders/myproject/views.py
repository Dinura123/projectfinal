from django.shortcuts import render

def index(request):
    return render(request,'myproject/index.html')

def about(request):
    return render(request,'myproject/about.html')

def Vehicle(request):
    return render(request,'myproject/Vehicle.html')

def contact(request):
    return render(request,'myproject/contact.html')

def signin(request):
    return render(request,'myproject/sign-in.html')

def signup(request):
    return render(request,'myproject/sign-up.html')






