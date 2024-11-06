<<<<<<< HEAD
from django.shortcuts import render
from time import gmtime, strftime, localtime #i will add local time, to get the data from my local pc

# Create your views here.
def displayTime(request):
    context = {
        "time": strftime("%Y-%m-%d %I:%M %p", localtime())
    }
    
=======
from django.shortcuts import render
from time import gmtime, strftime, localtime #i will add local time, to get the data from my local pc

# Create your views here.
def displayTime(request):
    context = {
        "time": strftime("%Y-%m-%d %I:%M %p", localtime())
    }
    
>>>>>>> 91d9e290e36a0fe0b3bbb2bb367710de86fc5dea
    return render(request,'index.html', context)