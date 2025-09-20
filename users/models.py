from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models

from materials.models import Course, Lesson


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="Почта", help_text="Укажите почту")

    phone = models.CharField(
        max_length=35, verbose_name="Телефон", blank=True, null=True, help_text="Введите номер телефона"
    )
    city = models.CharField(max_length=50, verbose_name="Город", blank=True, null=True, help_text="Введите город")
    avatar = models.ImageField(
        upload_to="users/avatars/", verbose_name="Аватар", blank=True, null=True, help_text="Загрузите аватар"
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email


class Payment(models.Model):
    PAYMENT_METHODS = [
        ("cash", "Наличные"),
        ("transfer", "Перевод на счет"),
        ("card", "Банковская карта"),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="payments", verbose_name="Пользователь"
    )
    payment_date = models.DateField(auto_now_add=True, verbose_name="Дата оплаты")
    paid_course = models.ForeignKey(
        Course,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="payments",
        verbose_name="Оплаченный курс",
    )
    paid_lesson = models.ForeignKey(
        Lesson,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="payments",
        verbose_name="Оплаченный урок",
    )
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Сумма оплаты")
    payment_method = models.CharField(max_length=10, choices=PAYMENT_METHODS, verbose_name="Способ оплаты")
    stripe_product_id = models.CharField(max_length=255, blank=True, null=True, verbose_name="Id продукта")
    stripe_price_id = models.CharField(max_length=255, blank=True, null=True, verbose_name="Id цены")
    stripe_session_id = models.CharField(max_length=255, blank=True, null=True, verbose_name="Id сессии")
    stripe_checkout_url = models.URLField(max_length=400, blank=True, null=True, verbose_name="Ссылка на оплату")
    stripe_payment_status = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return (f"{self.user.email} — {self.payment_amount} руб., {self.get_payment_method_display()} "
                f"({self.payment_date})")

    class Meta:
        verbose_name = "Платеж"
        verbose_name_plural = "Платежи"
