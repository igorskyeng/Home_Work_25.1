from rest_framework import serializers

from materials.models import Lesson, Course


class CourseSerializers(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = '__all__'


class LessonSerializers(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = '__all__'
