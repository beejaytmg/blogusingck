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

class Skill(models.Model):
    name = models.CharField(max_length=100)
    proficiency = models.IntegerField()  # You can use a range like 1 to 10

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    technology = models.ManyToManyField(Skill)
    github_link = models.URLField(blank=True, null=True)
    live_demo_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title

class Education(models.Model):
    institution = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)  # Can be null if ongoing
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.degree} at {self.institution}"

class Experience(models.Model):
    job_title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)  # Can be null if current
    responsibilities = models.TextField()

    def __str__(self):
        return f"{self.job_title} at {self.company}"

class Contact(models.Model):
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.email

class Resume(models.Model):
    name = models.CharField(max_length=100)
    summary = models.TextField()
    skills = models.ManyToManyField(Skill)
    projects = models.ManyToManyField(Project)
    education = models.ManyToManyField(Education)
    experience = models.ManyToManyField(Experience)
    contact = models.OneToOneField(Contact, on_delete=models.CASCADE)

    def __str__(self):
        return self.name