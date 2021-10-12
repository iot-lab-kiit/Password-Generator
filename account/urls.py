from django.urls import path, include
from . import views



urlpatterns = [
    path('signup/', views.AccoutView.as_view(), name='form'),
    path('login/', views.profile_login, name='login'),
    path('logout/', views.profile_logout, name='logout'),
    path('profile/', views.profile, name='profile'),
]
