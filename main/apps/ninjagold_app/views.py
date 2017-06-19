from django.shortcuts import render, redirect
import random

# Create your views here.

def index(request):
    if not 'gold' in request.session:
        request.session['gold'] = 0
    if not 'log' in request.session:
        request.session['log'] = ""
    
    data = {}
    data['gold'] = request.session['gold']
    data['log'] = request.session['log']
    return render(request, 'ninjagold_app/index.html')

def farm(request):
    if request.method == 'POST':
        rand = random.randrange(10,21)
        message = "<div class='won'> You visited the farm and got" + " " + str(rand) + " " + "coins!</div>"

        log = request.session['log']
        request.session['log'] = message + log
        request.session['gold'] += rand
        print request.session['log']
        return redirect('/')
    else:
        return redirect('/')

def cave(request):
    if request.method == 'POST':
        rand = random.randrange(5,11)
        message = "<div class='won'> You visited the cave and got" + " " + str(rand) + " " + "coins!</div>"

        log = request.session['log']
        request.session['log'] = message + log
        request.session['gold'] += rand
        print request.session['log']
        return redirect('/')
    else:
        return redirect('/')

def house(request):
    if request.method == 'POST':
        rand = random.randrange(2,6)
        message = "<div class='won'> You visited the house and got" + " " + str(rand) + " " + "coins!</div>"

        log = request.session['log']
        request.session['log'] = message + log
        request.session['gold'] += rand
        print request.session['log']
        return redirect('/')
    else:
        return redirect('/')

def casino(request):
    if request.method == 'POST':
        rand = random.randrange(-50,51)
        if rand < 0:
            request.session['outcome'] = 'lost'
        else: 
            request.session['outcome'] = "won"
        message = "<div class='" + request.session['outcome'] + "'> You visited the casino" + request.session['outcome'] + " " + str(rand) + " " + "coins!</div>"

        log = request.session['log']
        request.session['log'] = message + log
        request.session['gold'] += rand
        print request.session['log']
        return redirect('/')
    else:
        return redirect('/')
    
def reset(request):
    request.session.clear()
    return redirect('/')

