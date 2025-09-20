from datetime import timedelta

from celery import shared_task
from django.utils import timezone

from users.models import User


@shared_task
def deactivate_inactive_users():
    one_month_ago = timezone.now() - timedelta(days=30)
    users_to_deactivate = User.objects.filter(last_login__lt=one_month_ago, is_active=True)
    count = users_to_deactivate.update(is_active=False)
    return f"Заблокировано {count} пользователей."
