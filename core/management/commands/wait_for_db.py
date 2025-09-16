import time  # عشان نستخدم sleep
from psycopg2 import OperationalError as Psycopg2Error  # خطأ من psycopg2 لو DB مش جاهزة
from django.db.utils import OperationalError  # خطأ من Django لو DB مش جاهزة
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command to wait for database."""

    def handle(self, *args, **options):
        self.stdout.write('Waiting for database...')
        db_up = False  # نفترض البداية إن DB مش جاهزة

        while not db_up:  # نكرر المحاولة لغاية ما DB جاهزة
            try:
                self.check(databases=['default'])  # method check بتتحقق من DB
                db_up = True  # لو مفيش exception يبقى DB جاهزة
            except (Psycopg2Error, OperationalError):
                self.stdout.write('Database unavailable, waiting 1 second...')
                time.sleep(1)  # ننتظر ثانية قبل إعادة المحاولة

        self.stdout.write(self.style.SUCCESS('Database available!'))  # رسالة نجاح
