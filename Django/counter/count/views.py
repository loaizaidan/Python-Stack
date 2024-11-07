from django.shortcuts import *

from django.shortcuts import render

def index(request):
    if 'counter' in request.session:
        request.session['counter'] += 1
    else:
        request.session['counter'] = 0
    context = {
        'counter': request.session['counter']
    }
    return render(request, 'index.html', context)

def destroy_session(request):
    request.session.clear()
    return redirect('/')


def increment_by_2(request):
    if 'counter' in request.session:
        request.session['counter'] += 1
    else:
        request.session['counter'] = 1
    return redirect('/')


def reset(request):
    request.session.clear()
    return redirect('/')

