from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    """ SignUp form class definition"""
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter username '}), help_text=None)
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter password'}),
                                help_text=None, label='Password')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm password'}),
                                help_text=None, label='Confirm password')
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Enter email'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class LoginForm(forms.Form):
    """ Login form class definition """
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Enter Password'}))

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        try:
            user = User.objects.get(username=username)
            if user.check_password(password):
                return self.cleaned_data
            else:
                self.add_error('password', forms.ValidationError('Password incorrect'))
        except User.DoesNotExist:
            self.add_error('username', forms.ValidationError('User does not exists'))
