from django.core.management import BaseCommand
from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        user = User.objects.create(email="moderator@example.com")
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.set_password("123321try")
        user.save()
