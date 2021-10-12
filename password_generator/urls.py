from django.contrib import admin
from django.urls import path, include
from generator import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('generate/', views.home, name='home'),
    path('account/', include('account.urls')),
    path('password/', views.password, name='password'),
]
