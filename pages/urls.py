from django.urls import path
from .views import HomePageView, AboutPageView, PostDetailView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post_detail"),  # new
    path("about/", AboutPageView.as_view(), name="about"),
]