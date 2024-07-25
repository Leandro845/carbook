from celery import Celery
import os 

# Set the default settings module for Celery.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings')

# Create a Celery instance named 'main'.
app = Celery('main')

# Load Celery configuration from Django settings.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Auto-discover tasks in Django apps.
app.autodiscover_tasks()

# Debug task to print request information.
@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
