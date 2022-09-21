from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Peyami Safa',
        'title': '9. Hariciye Kogusu',
        'content': 'This is the content of book1',
        'date_posted': '21th September, 2022',
    },
    {
        'author': 'Jane Austen',
        'title': 'Pride and Prejudice',
        'content': 'This is the content of book2',
        'date_posted': '21th September, 1813',
    },
    {
        'author': 'José Saramago',
        'title': 'Blindness',
        'content': 'This is the content of book3',
        'date_posted': '21th September, 1995',
    },
]

# Create your views here.
def home(request):
    context = {
        'posts':posts
    }
    return render(request, 'blog/home.html', context)
def about(request):
    return render(request, 'blog/about.html')