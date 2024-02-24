from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
import uuid
import random
# Create your models here.
class event(models.Model):
    event_id = models.UUIDField(primary_key=True, default = uuid.uuid4)
    event_organizer = models.ForeignKey(User, on_delete=models.CASCADE)
    start = models.DateTimeField()
    end = models.DateTimeField()
    number_of_qr = models.IntegerField()
    event_active = models.BooleanField(blank = True, null = False)

    def __str__(self):
        return str(self.event_id)
    


# class qr(models.Model):
#     def qr_length(instance):
#         max_length = event.objects.get(event_id = instance.event.event_id).number_of_qr    
#         return "qr_templates/{0}".format(instance.event.event_id)
    
#     event = models.ForeignKey(event, on_delete=models.CASCADE)
#     template = models.ImageField(upload_to=qr_length)
class qr(models.Model):
    event = models.ForeignKey(event, on_delete=models.CASCADE)
    image = models.ImageField(blank = True, upload_to='media/qr')
    qr_id = models.UUIDField(default = uuid.uuid4,blank = True)
    hint = models.CharField(max_length = 100,blank = True)

# class eventForm(ModelForm):
#     class Meta:
#         model = event
#         fields = ['number_of_qr','start','end']

# class qrForm(ModelForm):
#     class Meta:
#         model = qr
#         fields = ['template']
