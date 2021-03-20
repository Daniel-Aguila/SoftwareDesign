from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name="home"),
    path('form/', views.form, name="form"),
    path('profile/',views.profile, name="profile"),
    path('login/',views.login, name="login"),
    path('signup/',views.signup, name="signup"),
]