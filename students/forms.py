from django import forms
from django.contrib.auth.forms import UserCreationForm
from users.models import User
from .models import StudentProfile

# Base User Form (Common fields)
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']

# Student Registration Form
class StudentRegisterForm(UserRegisterForm):
    full_name = forms.CharField(max_length=255)
    bio = forms.CharField(widget=forms.Textarea, required=False)

    class Meta(UserRegisterForm.Meta):
        fields = UserRegisterForm.Meta.fields + ['full_name', 'bio']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.user_type = 'student'
        if commit:
            user.save()
            StudentProfile.objects.create(user=user, full_name=self.cleaned_data['full_name'], bio=self.cleaned_data['bio'])
        return user
 