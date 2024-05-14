from django.db import models


NULLABLE = {'blank': True, 'null': True}


class Course(models.Model):
    course_name = models.CharField(max_length=150, verbose_name='Название курса')
    preview = models.ImageField(upload_to='materials/', **NULLABLE)
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.course_name

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
        ordering = ('id',)


class Lesson(models.Model):
    lesson_name = models.CharField(max_length=150, verbose_name='Название урока')
    course_name = models.ForeignKey(Course, verbose_name='Название урока', on_delete=models.CASCADE)
    preview = models.ImageField(upload_to='materials/', **NULLABLE)
    description = models.TextField(verbose_name='Описание')
    link_to_the_video = models.TextField(verbose_name='Ссылка на видео', **NULLABLE)

    def __str__(self):
        return self.lesson_name

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
        ordering = ('id',)
