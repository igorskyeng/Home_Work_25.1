import random

from django.conf import settings
from django.core.cache import cache
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy, reverse
from django.forms import inlineformset_factory

from pytils.translit import slugify
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated

from materials.models import Course, Lesson
from materials.paginators import LessonPaginator
from materials.permissions import IsModerator, IsOwner
from materials.serliazers import CourseSerializers, LessonSerializers


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializers

    def perform_create(self, serializer):
        new_course = serializer.save()
        new_course.owner = self.request.user
        new_course.save()

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [IsAuthenticated & ~IsModerator]

        elif self.action in ['retrieve', 'update', 'list']:
            self.permission_classes = [IsAuthenticated & (IsModerator | IsOwner)]

        elif self.action == 'destroy':
            self.permission_classes = [IsAuthenticated & IsOwner]

        return super().get_permissions()

    def get_queryset(self):
        if not self.request.user.is_staff:
            return Course.objects.filter(owner=self.request.user)

        elif self.request.user.is_staff:
            return Course.objects.all()


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializers
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated & ~IsModerator]

    def perform_create(self, serializer):
        new_lesson = serializer.save()
        new_lesson.owner = self.request.user
        new_lesson.save()


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializers
    permission_classes = [IsAuthenticated & (IsModerator | IsOwner)]
    pagination_class = LessonPaginator

    def get_queryset(self):
        if not self.request.user.is_staff:
            return Course.objects.filter(owner=self.request.user)

        elif self.request.user.is_staff:
            return Course.objects.all()


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializers
    permission_classes = [IsAuthenticated & (IsModerator | IsOwner)]

    def get_queryset(self):
        if not self.request.user.is_staff:
            return Course.objects.filter(owner=self.request.user)

        elif self.request.user.is_staff:
            return Course.objects.all()


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializers
    permission_classes = [IsAuthenticated & (IsModerator | IsOwner)]

    def get_queryset(self):
        if not self.request.user.is_staff:
            return Course.objects.filter(owner=self.request.user)

        elif self.request.user.is_staff:
            return Course.objects.all()


class LessonDestroyAPIView(generics.DestroyAPIView):
    serializer_class = LessonSerializers
    permission_classes = [IsAuthenticated & IsOwner]

    def get_queryset(self):
        if not self.request.user.is_staff:
            return Course.objects.filter(owner=self.request.user)

        elif self.request.user.is_staff:
            return Course.objects.all()
