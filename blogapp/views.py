from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import BlogPost

# List view for all blog posts
class BlogPostListView(ListView):
    model = BlogPost
    template_name = 'blogpost_list.html'  # Template to render
    context_object_name = 'posts'  # The name to use for the list in the template
    paginate_by = 20

# Detail view for a single blog post
class BlogPostDetailView(DetailView):
    model = BlogPost
    template_name = 'blogpost_detail.html'  # Template to render
