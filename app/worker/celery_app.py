from celery import Celery

from app.core.config import settings

celery = Celery('worker', broker=settings.redis_host)

from app.worker import tasks

# celery -A app.worker.celery_app worker --loglevel=info --pool=solo