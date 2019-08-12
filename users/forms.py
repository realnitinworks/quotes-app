from django_registration.forms import RegistrationForm

from .models import CustomUser


class CustomUserCreationForm(RegistrationForm):
    class Meta(RegistrationForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'age')


class CustomUserChangeFrom(RegistrationForm):
    class Meta(RegistrationForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'age')



