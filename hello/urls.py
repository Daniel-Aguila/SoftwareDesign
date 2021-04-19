from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name="home"),
    path('', include("django.contrib.auth.urls")),
    path('form/', views.form, name="form"),
    path('profile/',views.profile, name="profile"),
    path('signup/',views.signup, name="signup"),
    path('login/', views.loginpage, name="login"),
    path('logout/', views.logoutpage, name="logout"),
    path('history/', views.history, name="history"),
]
