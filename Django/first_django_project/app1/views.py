from django.shortcuts import render, HttpResponse, redirect 
from django.http import *
def root(request):
    return redirect("/blogs")

def index(request):
    return HttpResponse("placeholder to later display a list of all blogs")

def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")

def create(request):
    return HttpResponse("placeholde to later display a list of all blogs")

def show(request, number):
    return HttpResponse(f"placeholder to display blog number: {number}")

def edit(request, number):
    return HttpResponse(f"placeholder tp edit blog {number}")

def destroy(request, number):
    return redirect("/blogs")

def json_resp(request):
    return JsonResponse({"title": "My first blog", "content": "Occaecat non dolor qui officia laboris nulla commodo irure anim do anim nostrud."})