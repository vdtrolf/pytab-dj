# pages/views.py
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post

class HomePageView(ListView):
    model = Post
    template_name = "home.html"
  
class PostDetailView(DetailView):  
    model = Post
    template_name = "post_detail.html"

class PostCreateView(CreateView):  
    model = Post
    template_name = "post_new.html"
    fields = ["title", "author", "body"]
    
class PostEditView(UpdateView):  
    model = Post
    template_name = "post_edit.html"
    fields = ["title", "body"]    
    
class PostDeleteView(DeleteView):  # new
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy("home")    

class AboutPageView(TemplateView):
  template_name = "about.html"