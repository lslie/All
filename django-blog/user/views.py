from django.shortcuts import render


# Create your views here.


def index(request):
    return render(request, 'index.html')


def article(request):
    return render(request, 'page.html')


def contact(request):
    if request.method == 'GET':
        return render(request, 'contact.html')
    else:
        name = request.POST.get('name')
        email = request.POST.get('email')
        title = request.POST.get('subject')
        message = request.POST.get('message')
        return render(request, 'contact.html', {
            'name': name,
            'email': email,
            'title': title,
            'message': message,
        })
