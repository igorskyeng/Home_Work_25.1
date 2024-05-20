from django.contrib import admin
from materials.models import Course, Lesson
from users.models import Payments


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'course_name', 'preview', 'description')
    list_filter = ('course_name',)
    search_fields = ('course_name', 'description')


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('id', 'lesson_name', 'course', 'preview', 'description', 'link_to_the_video')
    list_filter = ('lesson_name',)
    search_fields = ('lesson_name', 'course_name')


@admin.register(Payments)
class PaymentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'payment_date', 'paid_course', 'payment_amount', 'payment_method')
    list_filter = ('paid_course',)
    search_fields = ('user', 'payment_date')
