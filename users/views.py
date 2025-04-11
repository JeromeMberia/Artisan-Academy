from django.shortcuts import render, redirect
from .forms import StudentRegisterForm, ArtisanRegisterForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import CustomLoginForm

def register_student(request):
    if request.method == "POST":
        form = StudentRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Auto login after registration
            return redirect("student_dashboard")  # Redirect to student page
    else:
        form = StudentRegisterForm()
    return render(request, "users/register_student.html", {"form": form})

def register_artisan(request):
    if request.method == "POST":
        form = ArtisanRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Auto login after registration
            return redirect("artisan_dashboard")  # Redirect to artisan page
    else:
        form = ArtisanRegisterForm()
    return render(request, "users/register_artisan.html", {"form": form})

# Student Login View
def student_login(request):
    if request.method == "POST":
        form = CustomLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user.user_type == "student":
                login(request, user)
                return redirect("student_dashboard")
            else:
                messages.error(request, "Invalid credentials.")
        else:
            messages.error(request, "Invalid email or password.")
    else:
        form = CustomLoginForm()

    return render(request, "users/student_login.html", {"form": form})

# Artisan Login View
def artisan_login(request):
    if request.method == "POST":
        form = CustomLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user.user_type == "artisan":
                login(request, user)
                return redirect("artisan_dashboard")
            else:
                messages.error(request, "Invalid credentials.")
        else:
            messages.error(request, "Invalid email or password.")
    else:
        form = CustomLoginForm()

    return render(request, "users/artisan_login.html", {"form": form})

def homepage(request):
    return render(request, "users/index.html")

