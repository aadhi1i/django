from django.contrib.auth.forms import UserCreationForm

from .models import customuser
class custform(UserCreationForm):
    class Meta:
        model = customuser
        fields = ('username','password1','password2','dob','profile','email')