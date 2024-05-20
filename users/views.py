import secrets

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import CreateView, UpdateView,  TemplateView
from django.urls import reverse_lazy, reverse
from django.core.mail import send_mail
from django.contrib.auth.views import LoginView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework import viewsets, generics

from users.models import User, Payments

from config.settings import EMAIL_HOST_USER
from users.serliazers import PaymentsSerializers


class UserLoginView(LoginView):
    pass


class PaymentsCreateAPIView(generics.CreateAPIView):
    serializer_class = PaymentsSerializers


class PaymentsListAPIView(generics.ListAPIView):
    serializer_class = PaymentsSerializers
    queryset = Payments.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('paid_course', 'payment_method')
    ordering_fields = ('payment_date',)


class PaymentsRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = PaymentsSerializers
    queryset = Payments.objects.all()


class PaymentsUpdateAPIView(generics.UpdateAPIView):
    serializer_class = PaymentsSerializers
    queryset = Payments.objects.all()


class PaymentsDestroyAPIView(generics.DestroyAPIView):
    serializer_class = PaymentsSerializers
    queryset = Payments.objects.all()
