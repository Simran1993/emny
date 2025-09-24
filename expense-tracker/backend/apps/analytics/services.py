from django.db import transaction
from django.utils import timezone
import logging

logger = logging.getLogger(__name__)

class BaseService:
    """Base service class with common functionality"""
    
    @staticmethod
    def get_current_timestamp():
        return timezone.now()
    
    @staticmethod
    def atomic_transaction(func):
        """Decorator for atomic database transactions"""
        return transaction.atomic(func)
