from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.conf import settings


# ---------------------------
# Custom User Model
# ---------------------------
class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_instructor = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    # Avoid clashes by setting related_name
    groups = models.ManyToManyField(
        Group,
        verbose_name=('groups'),
        blank=True,
        help_text=(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        related_name="core_user_set",
        related_query_name="core_user",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=('user permissions'),
        blank=True,
        help_text=('Specific permissions for this user.'),
        related_name="core_user_permissions_set",
        related_query_name="core_user_permission",
    )


# ---------------------------
# Student & Instructor Profiles
# ---------------------------
class Student(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    enrollment_date = models.DateField(auto_now_add=True)
    age = models.PositiveIntegerField(null=True, blank=True)

    def clean(self):
        if self.age is not None and (self.age < 10 or self.age > 18):
            raise ValueError("Age must be between 10 and 18")

    def __str__(self):
        return self.user.username


class Instructor(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    hire_date = models.DateField(auto_now_add=True)
    cv = models.FileField(upload_to='instructor_cvs/', null=True, blank=True)
    bio = models.TextField(blank=True, null=True)
    expertise = models.CharField(max_length=255, blank=True, null=True)
    age = models.PositiveIntegerField(null=True, blank=True)

    def clean(self):
        if self.age is not None and self.age < 18:
            raise ValueError("Instructor must be at least 18 years old")

    def __str__(self):
        return self.user.username


# ---------------------------
# Course & Rounds
# ---------------------------
class PublishStatus(models.TextChoices):
    RESERVE_NOW = 'Reserve Now', 'Reserve Now'
    COMING_SOON = 'Coming Soon', 'Coming Soon'
    ROUND_COMPLETED = 'Round Completed', 'Round Completed'


class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    instructor = models.ForeignKey(Instructor, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    status = models.CharField(
        max_length=20,
        choices=PublishStatus.choices,
        default=PublishStatus.RESERVE_NOW
    )

    image = models.ImageField(upload_to='course_images/', null=True, blank=True)

    def __str__(self):
        return self.name


class Round(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='rounds')
    name = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.course.name} - {self.name}"


class Week(models.Model):
    round = models.ForeignKey(Round, on_delete=models.CASCADE, related_name='weeks')
    number = models.PositiveIntegerField()
    title = models.CharField(max_length=255)

    def __str__(self):
        return f"Week {self.number} - {self.round.name}"


# ---------------------------
# Enrollments & Evaluations
# ---------------------------
class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    round = models.ForeignKey(Round, on_delete=models.CASCADE)
    enrolled_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.user.username} enrolled in {self.round.name}"


class WeeklyEvaluation(models.Model):
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE)
    week = models.ForeignKey(Week, on_delete=models.CASCADE)
    score = models.FloatField()
    feedback = models.TextField(blank=True)

    def __str__(self):
        return f"{self.enrollment.student.user.username} - Week {self.week.number}"


class RoundEvaluation(models.Model):
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE)
    total_score = models.FloatField()
    feedback = models.TextField(blank=True)

    def __str__(self):
        return f"{self.enrollment.student.user.username} - {self.enrollment.round.name} Evaluation"
