from django.core.management import BaseCommand
from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email='admin@duuuck.go',
            first_name='Admin',
            last_name='Duuuck_go',
            is_staff=True,
            is_superuser=True
        )

        user.set_password('11092003')
        user.save()
