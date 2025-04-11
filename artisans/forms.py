from django import forms
from django.contrib.auth.forms import UserCreationForm
from users.models import User
from .models import ArtisanProfile

# Base User Form
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']

# Artisan Registration Form
class ArtisanRegisterForm(UserRegisterForm):
    full_name = forms.CharField(max_length=255)
    bio = forms.CharField(widget=forms.Textarea, required=False)
    skills = forms.CharField(widget=forms.Textarea)
    experience_years = forms.IntegerField()

    class Meta(UserRegisterForm.Meta):
        fields = UserRegisterForm.Meta.fields + ['full_name', 'bio', 'skills', 'experience_years']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.user_type = 'artisan'
        if commit:
            user.save()
            ArtisanProfile.objects.create(
                user=user,
                full_name=self.cleaned_data['full_name'],
                bio=self.cleaned_data['bio'],
                skills=self.cleaned_data['skills'],
                experience_years=self.cleaned_data['experience_years']
            )
        return user