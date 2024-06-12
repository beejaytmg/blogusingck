from django.contrib.sitemaps import Sitemap
from .models import BlogPost

class BlogPostSitemap(Sitemap):
    changefreq = "weekly"  # How frequently the content is expected to change
    priority = 0.8  # The priority of this URL relative to other URLs on your site

    def items(self):
        return BlogPost.objects.all()  # Return all blog posts

    def lastmod(self, obj):
        return obj.updated_at  # Use the updated_at field for the last modified date

    def location(self, obj):
        return obj.get_absolute_url()  # Use the get_absolute_url method to get the URL
