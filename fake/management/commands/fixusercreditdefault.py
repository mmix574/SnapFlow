from django.core.management.base import BaseCommand,CommandError


class Command(BaseCommand):
    help = 'Command Line Template'

    def handle(self, *args, **options):
        print("Template Command Calling...")
        pass

