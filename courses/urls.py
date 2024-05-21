
from django.urls import path
from . import views
from .views import CourseView,MentorView

urlpatterns = [

    path("",CourseView.as_view(),name="courses"),
    path("mentors",MentorView.as_view(),name="mentors"),
  
]
