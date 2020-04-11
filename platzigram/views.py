# Django
from django.http import HttpResponse
#Utilities
from datetime import datetime

def hello_world(request):
    """return a greeting"""
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse('Oh, hi! current server time is {now}'.format(
        now=str(now)))

def hi(request):
    numbers = (request.GET['numbers'])
    return HttpResponse(str(numbers))
