from django.shortcuts import render

from django.http import HttpResponse
import datetime

#функция представления вьюшка
def current_datetime(request):
    now = datetime.datetime.now()
    html = f'<html><body>it is now {now}.</body></html>'
    return HttpResponse(html)

def greeting(request,name):
    return HttpResponse(f'h1')