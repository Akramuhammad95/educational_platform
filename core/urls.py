# core/urls.py
from django.urls import path
from .views import StudentRegisterView, InstructorRegisterView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("register/student/", StudentRegisterView.as_view(), name="student-register"),
    path("register/instructor/", InstructorRegisterView.as_view(), name="instructor-register"),
    path("login/", TokenObtainPairView.as_view(), name="login"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
