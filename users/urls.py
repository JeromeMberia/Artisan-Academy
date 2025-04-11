from django.urls import path
from .views import artisan_login, register_student, register_artisan, student_login, homepage

urlpatterns = [
    path("register/student/", register_student, name="register_student"),
    path("register/artisan/", register_artisan, name="register_artisan"),
    path("login/student/", student_login, name="student_login"),
    path("login/artisan/", artisan_login, name="artisan_login"),
    path("", homepage, name="home")   
]  
