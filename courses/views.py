from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Course,Mentor

# Create your views here.

class CourseView(ListView):
    model=Course

class MentorView(ListView):
    model=Mentor
