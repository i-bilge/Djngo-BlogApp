from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login

from .models import Post
from django.urls import reverse_lazy

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
    return render(request, 'blog/about.html', {'title':"About Page"})

# -------------------------------------------------
class PostList(LoginRequiredMixin, ListView):
    model = Post
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = context['post'].filter(user=self.request.user)
        return context

class PostDetail(LoginRequiredMixin, DetailView):
    model = Post
    context_object_name = 'post'
    
class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title','content']
    success_url = reverse_lazy('post')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PostCreate, self).form_valid(form)

class PostUpdate(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title','content']
    success_url = reverse_lazy("post")

class PostDelete(LoginRequiredMixin, DeleteView):
    model = Post
    context_object_name = 'post'
    success_url = reverse_lazy("post")

class CustomLoginView(LoginView):
    template_name = 'blog/login.html'
    fields = "__all__"
    redirect_authenticated_user: False

    def get_success_url(self):
        return reverse_lazy('post')

class RegisterPage(FormView):
    template_name = 'blog/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('post')