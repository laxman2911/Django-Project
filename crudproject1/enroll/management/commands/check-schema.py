from django.core.management.base import BaseCommand
from enroll.models import User
from django.db import connection

class Command(BaseCommand):
    help = 'Check the columns in the enroll_user table'

    def handle(self, *args, **kwargs):
        with connection.cursor() as cursor:
            cursor.execute("PRAGMA table_info(enroll_user);")
            columns = cursor.fetchall()
            for column in columns:
                self.stdout.write(f"Column: {column[1]}, Type: {column[2]}")
