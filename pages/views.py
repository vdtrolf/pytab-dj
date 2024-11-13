# pages/views.py
from django.views.generic import TemplateView, ListView, DetailView
from .models import Post

class HomePageView(ListView):
    model = Post
    template_name = "home.html"
  
class PostDetailView(DetailView):  # new
    model = Post
    template_name = "post_detail.html"

class AboutPageView(TemplateView):
  template_name = "about.html"