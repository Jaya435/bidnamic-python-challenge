from django.contrib.auth.models import User
from django.core.management import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        if not User.objects.filter(username="admin").exists():
            User.objects.create_user(
                username="admin",
                email="superuser@super.com",
                password="pass",
                is_staff=True,
                is_active=True,
                is_superuser=True,
            )
