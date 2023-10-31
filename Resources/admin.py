from django.contrib import admin
from .models import Course,Prerequisites,Learning,Video


# Register your models here.



class LearningAdmin(admin.TabularInline):
    model=Learning
class PrerequisitesAdmin(admin.TabularInline):
    model=Prerequisites

class VideoAdmin(admin.StackedInline):
    model=Video
class CourseAdmin(admin.ModelAdmin):
    inlines =[ LearningAdmin, PrerequisitesAdmin, VideoAdmin]





admin.site.register(Course,CourseAdmin)

admin.site.register(Video)