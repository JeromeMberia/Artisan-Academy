from django.shortcuts import render

from students.models import StudentProfile

def student_dashboard(request):
    student = StudentProfile.objects.get(user=request.user)
    
    return render(request, "students/student_dashboard.html", { 'student': student })
