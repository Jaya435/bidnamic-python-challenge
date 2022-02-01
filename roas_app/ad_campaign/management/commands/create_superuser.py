from django.core.management import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):

        User.objects.create_user(username='admin',
                                 email='superuser@super.com',
                                 password='pass',
                                 is_staff=True,
                                 is_active=True,
                                 is_superuser=True
                                 )
