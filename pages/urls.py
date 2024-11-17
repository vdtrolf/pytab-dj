from django.contrib import admin
from django.urls import path, include
from .views import HomePageView, AboutPageView, PostDetailView, PostCreateView, PostEditView, PostDeleteView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post_detail"),  
    path("post/new/", PostCreateView.as_view(), name="post_new"),  
    path("post/<int:pk>/edit/", PostEditView.as_view(), name="post_edit"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post_delete"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("accounts/", include("django.contrib.auth.urls")), 
]