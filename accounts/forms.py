from django import forms
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)

User = get_user_model()


class UserLoginForm(forms.Form):
    username = forms.CharField(label="User Name",
                               widget=forms.TextInput(attrs={'placeholder': 'User Name', 'class': 'btn btn-lg'}))
    password = forms.CharField(label="Password",
                               widget=forms.PasswordInput(attrs={'placeholder': 'User Name', 'class': 'btn btn-lg'}))

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("userame")
        password = self.cleaned_data.get("password")

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("This user does not exist")
            if not user.check_password(password):
                raise forms.ValidationError("Incorrect Passwords")
            if not user.is_active:
                raise forms.ValidationError("User account disabled, contact admin")

        return super(UserLoginForm, self).clean(*args, **kwargs)


class UserRegistration(forms.ModelForm):
    email = forms.EmailField(label="Email address",
                             widget=forms.EmailInput(
                                 attrs={'class': 'mdl-textfield__input', 'placeholder': 'Valid Email Address'}))
    email2 = forms.EmailField(label=" Confirm Email",
                              widget=forms.TextInput(
                                  attrs={'class': 'mdl-textfield__input', 'placeholder': 'Confirm Email Address'}))
    password = forms.CharField(label="Password",
                               widget=forms.PasswordInput(
                                   attrs={'class': 'mdl-textfield__input', 'placeholder': 'Password'}))

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'email2',
            'password',
        ]
        widgets = {
            "username": forms.TextInput(attrs={'class': 'mdl-textfield__input', 'placeholder': 'Username'}),
        }

    def clean_email2(self):
        email = self.cleaned_data.get("email")
        email2 = self.cleaned_data.get("email2")
        if email != email2:
            raise forms.ValidationError("Email do not match")
        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError("This email has already been registered")

        return email
