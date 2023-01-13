from django.shortcuts import render , redirect
from service.models import Post, Comment
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import UpdateView, DeleteView
from .forms import CommentForm, PostForm , UserRegisterForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

def index(req):
    return render(req, 'index.html')
@login_required
def abaut(req):
    return render(req, 'abaut.html')

class RegisterForm(CreateView):
    form_class  = UserRegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

class CreatePost(CreateView):
    model = Post
    template_name = "create_post.html"
    form_class = PostForm

class PostView( ListView):
    login_url = 'login'
    model = Post
    template_name = "index.html"
    ordering = ['-pk']

class detale_post(DetailView):
    model = Post
    templates_name = "post_detail.html"
    
    
class updatePost(LoginRequiredMixin,UpdateView):
    model = Post
    template_name = "create_post.html"
    form_class = PostForm

class DeletePost(LoginRequiredMixin,DeleteView):
    model = Post
    template_name = "delete_post.html"
    success_url = reverse_lazy('index')
    
class AddComment(LoginRequiredMixin,CreateView):
    model = Comment
    template_name = "add_comment.html"
    form_class = CommentForm

    def form_valid(self, form):
        form.instanse.post_id = self.kwargs['pk']
        return super().form_valid(form)
