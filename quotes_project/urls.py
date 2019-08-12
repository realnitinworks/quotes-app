"""quotes_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django_registration.backends.activation.views import RegistrationView
from users.forms import CustomUserCreationForm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/register/', RegistrationView.as_view(form_class=CustomUserCreationForm),
         name="django_registration_register"),  # For custom user signup, includes extra fields like 'age'
    path('users/', include('django_registration.backends.activation.urls')),
    path('users/', include('django.contrib.auth.urls')),
    path("", include("quotes.urls")),
]
