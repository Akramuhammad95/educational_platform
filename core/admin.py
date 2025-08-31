from django.contrib import admin
from .models import User, Student, Instructor, Course, Round, Week, Enrollment, WeeklyEvaluation, RoundEvaluation

admin.site.register(User)
admin.site.register(Student)
admin.site.register(Instructor)
admin.site.register(Course)
admin.site.register(Round)
admin.site.register(Week)
admin.site.register(Enrollment)
admin.site.register(WeeklyEvaluation)
admin.site.register(RoundEvaluation)
