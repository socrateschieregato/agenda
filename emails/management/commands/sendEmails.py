from django.core.management.base import BaseCommand, CommandError
from emails.views import sendEmails_cmd


class Command(BaseCommand):
    help = 'Send emails every day'

    def handle(self, **options):
        email = sendEmails_cmd()
        self.stdout.write(self.style.SUCCESS(email))

