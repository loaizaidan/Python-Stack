from django.shortcuts import  * 
from django.http import * 


def root(request):
    return redirect("/")

def index(request):
    return render(request, 'index.html')

def survey_result(request):
    if request.method == "GET":
        return redirect("/")
    elif request.method == "POST":
            request.session['name'] = request.POST['name']
            request.session['favorite_language'] =  request.POST['favorite_language']
            request.session['dojo_location'] =  request.POST['dojo_location']
            request.session['comment'] =  request.POST['comment']
            return render(request, "result.html" )
    
