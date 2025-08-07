
from django.shortcuts import render

# Create your views here.
def landing(request):
    return render(request, 'single_pages/landing.html', {
        'title': 'Landing',
        'name': '김윤석',
    })


def about(request):
    return render(request,'single_pages/aboutme.html',
                  {'title': 'About'})