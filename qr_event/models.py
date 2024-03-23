from django.db import models
from setup.models import event
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
# class player(models.Model):
#     event = models.ForeignKey(event, on_delete = models.CASCADE)
#     player = models.ForeignKey(User,on_delete = models.CASCADE)
#     collected = models.BooleanField(default = False)
#     time = models.DateTimeField(default = timezone.now)
#     def __str__(self):
#         return self.event_code