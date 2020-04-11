# Django
from django.http import HttpResponse
#Utilities
from datetime import datetime
import json

def hello_world(request):
    """return a greeting"""
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse('Oh, hi! current server time is {now}'.format(
        now=str(now)))

def sort_ints(request):
    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    sorted_int = sorted(numbers)
    data = {
        'status': 'ok',
        'numbers': sorted_int,
        'message': 'Intergers sorted successfully'

    }
    return HttpResponse(
        json.dumps(data, indent=4),
        content_type='application/json')

def say_hi(request, name, age):
    if age < 12:
        message = 'Sorry {}, you are not allowed here'.format(name)
    else:
        message = 'Helllo {}, welcome to platzigram'.format(name)
    return HttpResponse(message)
