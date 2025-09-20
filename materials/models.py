from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=150, verbose_name="Название курса")
    preview = models.ImageField(upload_to="courses/preview", blank=True, null=True, verbose_name="Превью")
    description = models.TextField(verbose_name="Описание курса")
    owner = models.ForeignKey(
        "users.User", on_delete=models.SET_NULL, verbose_name="Создатель курса", blank=True, null=True
    )
    updated_at = models.DateTimeField(auto_now=True)
    last_notification_sent = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"
        ordering = ["name"]


class Lesson(models.Model):
    name = models.CharField(max_length=150, verbose_name="Название урока")
    description = models.TextField(verbose_name="Описание урока")
    preview = models.ImageField(upload_to="lessons/preview", blank=True, null=True, verbose_name="Превью")
    url = models.URLField(max_length=300, verbose_name="Ссылка на видео")
    course = models.ForeignKey(Course, related_name="lessons", on_delete=models.CASCADE)
    owner = models.ForeignKey(
        "users.User", on_delete=models.SET_NULL, verbose_name="Создатель урока", blank=True, null=True
    )
    updated_at = models.DateTimeField(auto_now=True)
    last_notification_sent = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Урок: {self.name} (Курс: {self.course.name})"

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
        ordering = ["name"]


class Subscription(models.Model):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="subscriptions")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="subscriptions")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "course")
        verbose_name = "Подписка"
        verbose_name_plural = "Подписки"

    def __str__(self):
        return f"{self.user} подписан на {self.course} с {self.created_at}"
