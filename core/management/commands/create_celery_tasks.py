from django.core.management.base import BaseCommand
from django_celery_beat.models import PeriodicTask, IntervalSchedule
import json

class Command(BaseCommand):
    help = 'Create Celery Beat periodic tasks'

    def handle(self, *args, **kwargs):
        schedule, created = IntervalSchedule.objects.get_or_create(
            every=30,
            period=IntervalSchedule.SECONDS,
        )

        PeriodicTask.objects.get_or_create(
            interval=schedule,
            name='my_interval_task_schedule',
            task='core.tasks.test_beat',  # The task's full path
        )

        self.stdout.write(self.style.SUCCESS('Successfully created tasks'))
