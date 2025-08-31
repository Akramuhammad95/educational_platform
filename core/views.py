from django.shortcuts import render
from education import models

# Create your views here.

def dashboard(request):
    courses = models.Course.objects.all()
    students = models.Student.objects.all() 
    instructors = models.Instructor.objects.all()
    weaks = models.Week.objects.all()
    enrollments = models.Enrollment.objects.all()
    certificates = models.Certificate.objects.all()
    assignments = models.Assignment.objects.all()
    submissions = models.Submission.objects.all()

    context = {

        'courses': courses,
        'students': students,
        'instructors': instructors,
        'weaks': weaks,
        'enrollments': enrollments,
        'certificates': certificates,
        'assignments': assignments,
        'submissions': submissions,


    }
    return render(request, 'core/dashboard.html', context)
