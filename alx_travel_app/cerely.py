# alx_travel_app/celery.py
import os
from celery import Celery
from django.conf import settings

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'alx_travel_app.settings')

# Create the Celery application
app = Celery('alx_travel_app')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

# Optional: Add periodic tasks
app.conf.beat_schedule = {
    # Example: Run every 30 minutes
    # 'send-email-notifications': {
    #     'task': 'listings.tasks.send_email_notifications',
    #     'schedule': 30.0 * 60,  # 30 minutes
    # },
}

app.conf.timezone = 'UTC'


@app.task(bind=True)
def debug_task(self):
    """Debug task for testing Celery configuration."""
    print(f'Request: {self.request!r}')
    return 'Debug task completed successfully!'