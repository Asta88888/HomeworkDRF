from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail

from materials.models import Subscription, Course


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
