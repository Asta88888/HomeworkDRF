from datetime import timedelta

from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail
from django.utils import timezone

from materials.models import Subscription, Course
from users.models import User


@shared_task
def send_update_notification(course_id):
    course = Course.objects.get(id=course_id)
    subscriptions = Subscription.objects.filter(course=course).select_related("user")

    for sub in subscriptions:
        if sub.user.email:
            send_mail(
                subject=f"Обновление курса {course.name}",
                message=f"Курс «{course.name}» был обновлён. Проверьте новые материалы.",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[sub.user.email],
                fail_silently=False,
            )


@shared_task
def deactivate_inactive_users():
    one_month_ago = timezone.now() - timedelta(days=30)
    users_to_deactivate = User.objects.filter(
        last_login__lt=one_month_ago,
        is_active=True
    )
    count = users_to_deactivate.update(is_active=False)
    return f'Заблокировано {count} пользователей.'