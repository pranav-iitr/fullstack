from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User
from datetime import datetime,timedelta

