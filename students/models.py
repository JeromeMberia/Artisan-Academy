from django.db import models
from users.models import User
from courses.models import Course

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="student_profile")
    full_name = models.CharField(max_length=255)
    bio = models.TextField(blank=True, null=True)
    enrolled_courses = models.ManyToManyField(Course, blank=True, related_name="students_enrolled")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name

