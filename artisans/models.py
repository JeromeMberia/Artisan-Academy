from django.db import models
from users.models import User

class ArtisanProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="artisan_profile")
    full_name = models.CharField(max_length=255)
    bio = models.TextField(blank=True, null=True)
    skills = models.TextField()  # List of skills
    experience_years = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name
