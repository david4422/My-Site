from django.urls import path
from . import views

urlpatterns = [
    path("" , views.Blog.as_view(), name="starting-page"),
    path("posts", views.BlogList.as_view(), name="posts-page"),
    path("posts/<slug:slug>", views.BlogDetails.as_view(), name="details-page"), #my-first-blog,
    path("read-later", views.ReadLaterView.as_view(), name="read-later")

]