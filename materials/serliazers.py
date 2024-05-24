from rest_framework import serializers

from materials.models import Lesson, Course


class LessonSerializers(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializers(serializers.ModelSerializer):
    number_of_lessons = serializers.SerializerMethodField()
    lessons = LessonSerializers(source='lesson_set', many=True, read_only=True)

    class Meta:
        model = Course
        fields = '__all__'

    @staticmethod
    def get_number_of_lessons(instance):
        return instance.lesson_set.all().count()
