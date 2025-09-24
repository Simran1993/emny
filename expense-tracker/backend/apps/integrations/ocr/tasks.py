from celery import shared_task
from django.utils import timezone
import logging

logger = logging.getLogger(__name__)

@shared_task
def sample_task():
    """Sample Celery task"""
    logger.info("Sample task executed at %s", timezone.now())
    return "Task completed successfully"
