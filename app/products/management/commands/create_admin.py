from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Create an admin with username "admin" and password "admin"'

    def handle(self, *args, **kwargs):
        # Check if the admin user already exists
        if User.objects.filter(username='admin').exists():
            self.stdout.write(self.style.WARNING('Admin user already exists.'))
            return

        # Create the admin user
        User.objects.create_superuser('admin', 'admin@example.com', 'admin')
        self.stdout.write(self.style.SUCCESS('Admin user created successfully.'))
