from django.shortcuts import render, get_object_or_404
from datetime import date
from blog.models import Author, Post, Tag
from django.views.generic import ListView, DetailView
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic.base import TemplateView
from .forms import CommentForm


class Blog(ListView):
    template_name = "blog/starting_page.html"
    model = Post
    ordering = ["-date" ]
    context_object_name = "posts"

    def get_queryset(self):
        query =  super().get_queryset()
        data = query[:3]
        return data

class BlogList(ListView):
    template_name = "blog/posts.html"
    model = Post
    ordering = ["-date" ]
    context_object_name = "all_posts"

class BlogDetails(View):

    def get(self, request, slug):
        post = Post.objects.get(slug = slug)
        context = {
            "post": post,
            "post_tags" : post.tag.all(),
            "comment_form" : CommentForm(),
            "comments" : post.comments.all().order_by("-id")
        }
        return render(request,  "blog/post_details.html", context)


    def post(self, request , slug):
        comment_form = CommentForm((request.POST))
        post = Post.objects.get(slug = slug)


        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse("details-page" , args=[slug]))

        context = {
            "post": post,
            "post_tags" : post.tag.all(),
            "comment_form" : comment_form,
            "comments" : post.comments.all().order_by("-id")
        }
        return render(request,  "blog/post_details.html", context)


   

# Create your views here.
# def starting_page(request):
#     latest_posts = Post.objects.all().order_by("-date")[:3]
#     return render(request, "blog/starting_page.html", {
#         "posts" : latest_posts
#     })

# def posts(request):
#     all_posts = Post.objects.all()
#     return render(request, "blog/posts.html", {
#         "all_posts" :all_posts
#     })

# def post_detail(request, slug):
#     identify_post = Post.objects.all().get(slug = slug)
#     return render(request, "blog/post_details.html" , {
#          "post" : identify_post,
#          "post_tags" : identify_post.tag.all()
#     })


