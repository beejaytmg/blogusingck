from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import BlogPost
from django.http import HttpResponse, request
from django.conf import settings
import os
def favicon(request):
    with open('favicon.ico', 'rb') as f:
        return HttpResponse(f.read(), content_type='image/x-icon')

def ads_txt(request):
    ads_file_path = os.path.join(settings.BASE_DIR, 'ads.txt')
    try:
        with open(ads_file_path, 'r') as file:
            content = file.read()
        return HttpResponse(content, content_type='text/plain')
    except FileNotFoundError:
        return HttpResponse('File not found.', status=404, content_type='text/plain')
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
def iframe_player(request):
    # If 'src' is provided in the URL parameter, use it; otherwise, get it from the form
    src = request.GET.get('src', None)
    
    if src:
        return render(request, 'iframe_player.html', {'src': src})