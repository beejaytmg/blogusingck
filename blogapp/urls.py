from django.urls import path
from .views import BlogPostListView, BlogPostDetailView, ads_txt, src_redirect, favicon, robots_txt, error_page
urlpatterns = [
    path('', BlogPostListView.as_view(), name='blogpost_list'),
    path('post/<slug:slug>/', BlogPostDetailView.as_view(), name='blogpost_detail'),
    path('ads.txt', ads_txt, name='ads-txt'),
    path('robots.txt', robots_txt, name='ads-txt'),
    path('favicon.ico', favicon, name='favicon'),
    path('src/', src_redirect, name='iframe_player'),
    path('error/', error_page, name='error'),
]
