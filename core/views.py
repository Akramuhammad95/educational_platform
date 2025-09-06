# core/views.py
from rest_framework import generics
from rest_framework.permissions import AllowAny
from .serializers import StudentRegisterSerializer, InstructorRegisterSerializer
from .models import Student, Instructor

class StudentRegisterView(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentRegisterSerializer
    permission_classes = [AllowAny]

class InstructorRegisterView(generics.CreateAPIView):
    queryset = Instructor.objects.all()
    serializer_class = InstructorRegisterSerializer
    permission_classes = [AllowAny]
