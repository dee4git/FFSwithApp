from django.http import HttpResponse
from django.shortcuts import render
def about (request):
    #return HttpResponse("About is working")
    return render(request,'about.html')
def home (request) :
    #return HttpResponse("This is a homepage")
    return render(request,'home.html')
def makeMoney (request) :
    return render (request,'makeMoney.html')
def login (request) :
    return render (request,'login.html')
