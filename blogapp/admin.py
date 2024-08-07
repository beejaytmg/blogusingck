from django.contrib import admin
from .models import BlogPost
from .models import Skill, Project, Education, Experience, Contact, Resume

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'proficiency')
    search_fields = ('name',)
    list_filter = ('proficiency',)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    search_fields = ('title',)
    filter_horizontal = ('technology',)

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('institution', 'degree', 'start_date', 'end_date')
    search_fields = ('institution', 'degree')
    list_filter = ('start_date', 'end_date')

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('job_title', 'company', 'start_date', 'end_date')
    search_fields = ('job_title', 'company')
    list_filter = ('start_date', 'end_date')

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('email', 'phone')
    search_fields = ('email', 'phone')

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('name', 'summary')
    search_fields = ('name',)
    filter_horizontal = ('skills', 'projects', 'education', 'experience')
    readonly_fields = ('contact',) 
# Register your models here.
admin.site.register(BlogPost)
