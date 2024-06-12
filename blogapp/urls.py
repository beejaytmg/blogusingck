from django.urls import path
from .views import BlogPostListView, BlogPostDetailView, ads_txt, iframe_player
urlpatterns = [
    path('', BlogPostListView.as_view(), name='blogpost_list'),
    path('post/<slug:slug>/', BlogPostDetailView.as_view(), name='blogpost_detail'),
    path('ads.txt', ads_txt, name='ads-txt'),
    path('src/', iframe_player, name='iframe_player'),
]
