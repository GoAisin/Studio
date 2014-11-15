__author__ = 'victory'
from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello Studio")