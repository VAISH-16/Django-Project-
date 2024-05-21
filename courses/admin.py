from django.contrib import admin
from .models import Course,Category,Tag,Mentor

# Register your models here.
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display=['id','course_name','course_description','course_price','course_picture','mentor','category']
# Registering Course model on the admin panel
# admin.site.register(Course,CourseAdmin)  Method 1
# @admin.register(Course) Method 2

# ---------------------------
# Registering Category


class CategoryAdmin(admin.ModelAdmin):
    list_display=['id','category_name']

admin.site.register(Category,CategoryAdmin)

class TagAdmin(admin.ModelAdmin):
    list_display=['id','tag_name']

admin.site.register(Tag,TagAdmin)

class MentorAdmin(admin.ModelAdmin):
    list_display=['id','mentor_name','mentor_speciality','mentor_salary','mentor_schedule_time','mentor_experience','mentor_picture']

admin.site.register(Mentor,MentorAdmin)