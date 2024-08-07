from django.urls import path, include
from .views import BlogPostListView, BlogPostDetailView, ads_txt, src_redirect, favicon, robots_txt, error_page
from rest_framework.routers import DefaultRouter
from .views import SkillViewSet, ProjectViewSet, EducationViewSet, ExperienceViewSet, ContactViewSet, ResumeViewSet

router = DefaultRouter()
router.register(r'skills', SkillViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'education', EducationViewSet)
router.register(r'experience', ExperienceViewSet)
router.register(r'contacts', ContactViewSet)
router.register(r'resumes', ResumeViewSet)
urlpatterns = [
    path('', BlogPostListView.as_view(), name='blogpost_list'),
    path('post/<slug:slug>/', BlogPostDetailView.as_view(), name='blogpost_detail'),
    path('ads.txt', ads_txt, name='ads-txt'),
    path('robots.txt', robots_txt, name='ads-txt'),
    path('favicon.ico', favicon, name='favicon'),
    path('src/', src_redirect, name='iframe_player'),
    path('error/', error_page, name='error'),
    path('api/', include(router.urls)),
]
