from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import ArtisanRegisterForm

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
