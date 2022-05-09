from django.shortcuts import redirect
from django.urls import reverse_lazy,reverse
from django.views.generic import CreateView, FormView, View
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, LoginForm


class SignUpView(SuccessMessageMixin, CreateView):
    """ User sign up view definition"""
    template_name = 'accounts/signup.html'
    form_class = SignUpForm
    success_url = reverse_lazy('accounts:signup')
    success_message = 'Registration Successful !!'


class LoginView(SuccessMessageMixin, FormView):
    """ User login view definition"""
    template_name = 'accounts/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('todos:home')
    success_message = 'Login Successful !!'

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)


class LogoutView(View):
    """Log out view definition """
    def get(self, request):
        logout(request)
        messages.success(request,'Logout successful !!')
        return redirect(reverse('todos:home'))

