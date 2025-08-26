# education/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('my-courses/', views.my_courses, name='my_courses'),
    path('my-courses/<int:pk>/', views.course_detail, name='course_detail'),
    path('my-courses/<int:pk>/assignments/', views.course_assignments, name='course_assignments'),
    path('my-courses/<int:pk>/grades/', views.course_grades, name='course_grades'),
]
