from django.shortcuts import render,HttpResponse

# Create your views here.

def show_news_index(request):
    return HttpResponse("新闻")