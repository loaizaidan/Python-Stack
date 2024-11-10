from django.shortcuts import *
from django.http import * 
import random
from django.contrib import *
from datetime import *

def index(request):
    
    if 'gold' not in request.session:
        request.session['gold'] = 0
        request.session['activities'] = []
    if 'attempts' not in request.session:
        request.session['attempts'] = 0
    context= {
         'gold': request.session['gold'],
         'activities':request.session['activities'], 
         'attempts':request.session['attempts']
    }
   
    return render(request ,'index.html', context)



def process_money(request):
    building = request.POST['building']
    gold_earned = 0

    if building == 'farm':
        gold_earned = random.randint(10, 30)
    elif building == 'cave':
        gold_earned = random.randint(15, 20)
    elif building == 'house':
        gold_earned = random.randint(13, 40)
    elif building == 'casino':
        gold_earned = random.randint(-50, 50)

    request.session['gold'] += gold_earned
    request.session['attempts'] += 1

    now = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    if gold_earned >



