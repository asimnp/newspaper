from django.contrib.auth.forms import AdminUserCreationForm, UserChangeForm

from .models import CustomUser


class CustomUserCreationForm(AdminUserCreationForm):
    class Meta:
        model = CustomUser
        fields = (
            "username",
            "email",
        )


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = (
            "username",
            "email",
        )


class SignupForm(CustomUserCreationForm):
    def __init__(self, *arg, **kwargs):
        super().__init__(*arg, **kwargs)
        # Remove password-based authentication
        if "usable_password" in self.fields:
            del self.fields["usable_password"]

        self.fields["email"].required = True
