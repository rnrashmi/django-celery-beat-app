from django.http import HttpResponse
from django.shortcuts import render
from core.tasks import demo

# Create your views here.

def excute_task(request):
    print('executing task')
    demo.delay()
    return HttpResponse({'status': 'success'})
