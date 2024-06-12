from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone
from django.urls import reverse

class BlogPost(models.Model):
    title = models.CharField(max_length=200)  # Title of the blog post
    meta_description = models.CharField(max_length=160, blank=True)  # Meta description for SEO
    content = RichTextField()  # Content field using CKEditor
    published_date = models.DateTimeField(default=timezone.now)  # Published date with a default value of the current time
    slug = models.SlugField(unique=True, max_length=200)  # Slug for the URL
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)  # Reference to the user who authored the post
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for when the post was created
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp for when the post was last updated

    class Meta:
        ordering = ['-published_date']  # Order by published date descending

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blogpost_detail', kwargs={'slug': self.slug})

# Example usage:
# You will typically have a view and URL configuration that matches the get_absolute_url method
# so that calling blogpost.get_absolute_url() returns a valid URL for the blog post detail view.
