from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название курса')
    preview = models.ImageField(upload_to='courses/preview', blank=True, null=True, verbose_name='Превью')
    description = models.TextField(verbose_name='Описание курса')


    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
        ordering = ['name']


class Lesson(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название урока')
    description = models.TextField(verbose_name='Описание урока')
    preview = models.ImageField(upload_to='lessons/preview', blank=True, null=True, verbose_name='Превью')
    url = models.URLField(max_length=300, verbose_name='Ссылка на видео')
    course = models.ForeignKey(Course, related_name='lessons', on_delete=models.CASCADE)


    def __str__(self):
        return f'Урок: {self.name} (Курс: {self.course.name})'


    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
        ordering = ['name']
