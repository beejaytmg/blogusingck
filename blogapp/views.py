from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import BlogPost
from django.http import HttpResponse, request
from django.conf import settings
import os
import random
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
def robots_txt(request):
    ads_file_path = os.path.join(settings.BASE_DIR, 'robots.txt')
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
    template_name = 'blogpost_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        video_url = self.request.session.get('video_url')
        if video_url:
            context['video_url'] = video_url
            # Optionally, remove the video_url from session after fetching
            del self.request.session['video_url']
        return context

def get_random_blog_post():
    blog_posts = BlogPost.objects.all()
    if blog_posts:
        return random.choice(blog_posts)
    return None
def src_redirect(request):
    video_url = request.GET.get('src')
    random_post = get_random_blog_post()
    if video_url:
        # Print video_url for debugging
        print("Video URL provided:", video_url)
        
        # Store the video URL in the session
        request.session['video_url'] = video_url
        
        # Check if the video URL is set in session
        print("Video URL stored in session:", request.session.get('video_url'))
        
        # Redirect to the video player view
        return redirect(random_post.get_absolute_url())
    else:
        # Redirect to the error page with a query parameter
        return redirect(f'/error/?message=No video URL provided')

# def video_player(request):
#     # Retrieve the video URL from the session
#     video_url = request.session.get('video_url')
    
#     # Print video_url for debugging
#     print("Retrieved Video URL from session:", video_url)
    
#     return render(request, 'video_player.html', {'video_url': video_url})

def error_page(request):
    message = request.GET.get('message', 'An error occurred')
    return render(request, 'error.html', {'message': message})

