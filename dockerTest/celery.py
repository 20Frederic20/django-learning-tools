from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Définir le module de paramètres Django par défaut pour 'celery'
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dockerTest.settings")

app = Celery("dockerTest")

# Charger les paramètres de configuration de Django
app.config_from_object("django.conf:settings", namespace="CELERY")

# Découvrir automatiquement les tâches
app.autodiscover_tasks()
