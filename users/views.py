import secrets

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import CreateView, UpdateView,  TemplateView
from django.urls import reverse_lazy, reverse
from django.core.mail import send_mail
from django.contrib.auth.views import LoginView

from users.models import User

from config.settings import EMAIL_HOST_USER


class LoginView(LoginView):
    pass
