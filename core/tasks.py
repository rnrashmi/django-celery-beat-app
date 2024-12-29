
from dj_celery.celery import app
import time
from celery import shared_task

@app.task()
def demo():
    time.sleep(1)
    print('aync task done by clery!!!')
    return 'app Task Async'

@shared_task()
def test_beat():
    print('beat task ran!!')
    return 'Shared Task Async'