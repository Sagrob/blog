from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Author

class AuthorCreationForm(UserCreationForm):
    class Meta:
        model = Author
        fields = ['username', 'email', 'password1', 'password2']

class AuthenticationForm(AuthenticationForm):
    class Meta:
        model = Author
        fields = ['username', 'password']