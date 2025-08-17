from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from materials.models import Course, Lesson
from users.models import Payment
from datetime import date


class Command(BaseCommand):
    help = 'Создает пользователя, курс, урок, платеж'

    def handle(self, *args, **kwargs):
        User = get_user_model()
        user, created = User.objects.get_or_create(
            email='withoutperms@example.com',
            defaults={
                'first_name': 'Without',
                'last_name': 'Perms',
                'city': 'Санкт-Петербург',
                'phone': '+79999999999',
                'is_active': True,
            }
        )
        if created:
            user.set_password('147852369t')
            user.save()
            self.stdout.write(self.style.SUCCESS(f'Пользователь {user.email} создан'))
        else:
            self.stdout.write(self.style.WARNING(f'Пользователь {user.email} уже существует'))

        course, created = Course.objects.get_or_create(
            name='Python для начинающих',
            defaults={
                'description': 'Python для начинающих — это простой и читаемый язык программирования, который подходит для первых шагов в IT.'
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS(f'Курс {course.name} создан'))
        else:
            self.stdout.write(self.style.WARNING(f'Курс {course.name} уже существует'))

        lesson, created = Lesson.objects.get_or_create(
            name="Введение в Python",
            course=course,
            defaults={
                "description": "Первый урок по Python",
                "url": "https://example.com/python-intro"
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS(f'Урок {lesson.name} создан'))
        else:
            self.stdout.write(self.style.WARNING(f'Урок {lesson.name} уже существует'))

        payment1, created = Payment.objects.get_or_create(
            user=user,
            payment_date=date(2025, 8, 13),
            paid_course=course,
            paid_lesson=None,
            payment_amount=1000.00,
            payment_method="cash"
        )
        if created:
            self.stdout.write(self.style.SUCCESS(f"Платеж №{payment1.id} за курс создан"))
        else:
            self.stdout.write(self.style.WARNING(f'Платеж №{payment1.id} уже существует'))

        payment2, created = Payment.objects.get_or_create(
            user=user,
            payment_date=date(2025, 8, 10),
            paid_course=None,
            paid_lesson=lesson,
            payment_amount=500.00,
            payment_method="transfer"
        )
        if created:
            self.stdout.write(self.style.SUCCESS(f"Платеж №{payment2.id} за урок создан"))
        else:
            self.stdout.write(self.style.WARNING(f'Платеж №{payment2.id} уже существует'))
