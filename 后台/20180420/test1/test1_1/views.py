from django.shortcuts import render,HttpResponse
import time
# Create your views here.

def show_time(request):
    return HttpResponse(time.ctime())