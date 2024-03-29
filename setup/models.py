from django.db import models, IntegrityError
from django.contrib.auth.models import User
from django.forms import ModelForm
import uuid
from django.utils import timezone

# Create your models here.
class event(models.Model):
    def generate_unique_value():
        uid = str(uuid.uuid4())
        sp = uid.split('-')[-1]
        return sp


    event_id = models.UUIDField(primary_key=True, default = uuid.uuid4)
    event_organizer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="event")
    start = models.DateTimeField()
    end = models.DateTimeField()
    number_of_qr = models.IntegerField()
    event_active = models.BooleanField(blank = True, null = False)
    event_code = models.CharField(max_length = 12, unique = True, default = generate_unique_value)
    

    def save(self, *args, **kwargs):
        # Attempt to save the model
        try:
            super(event, self).save(*args, **kwargs)
        except IntegrityError:
            # If IntegrityError occurs (non-unique value), generate a new unique value and try again
            self.event_code = self.generate_unique_value()
            super(event, self).save(*args, **kwargs)
    
    def __str__(self):
        return str(self.event_id)
    


# class qr(models.Model):
#     def qr_length(instance):
#         max_length = event.objects.get(event_id = instance.event.event_id).number_of_qr    
#         return "qr_templates/{0}".format(instance.event.event_id)
    
#     event = models.ForeignKey(event, on_delete=models.CASCADE)
#     template = models.ImageField(upload_to=qr_length)
    
# class player(models.Model):
#     event = models.ForeignKey(event, on_delete=models.CASCADE)
#     player = models.ForeignKey(User, on_delete=models.CASCADE)
#     joined_at = models.DateTimeField(default=timezone.now)

#     def __str__(self):
#         return f"{self.player.username} ({self.event.event_code})"

class qr(models.Model):
    event = models.ForeignKey(event, on_delete=models.CASCADE)
    image = models.ImageField(blank = True, upload_to='qr')
    qr_id = models.UUIDField(primary_key=True, default = uuid.uuid4, blank = True)
    hint = models.CharField(max_length = 100, blank = True)

    def __str__(self):
        return str(self.event)

class player(models.Model):
    event = models.ForeignKey(event, on_delete=models.CASCADE)
    player = models.ForeignKey(User, on_delete=models.CASCADE)
    joined_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.player.username} ({self.event.event_code})"


class scanned_qr(models.Model):
    qr_id = models.ForeignKey('qr', on_delete=models.CASCADE)  # Foreign key to the qr model
    scanned_by = models.ForeignKey(User, on_delete=models.CASCADE)  # Foreign key to the user (player)
    email = models.EmailField(blank=True,null=True)
    scanned_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.qr_id} scanned by {self.scanned_by.email}"  # Use email for identification


# class eventForm(ModelForm):
#     class Meta:
#         model = event
#         fields = ['number_of_qr','start','end']

# class qrForm(ModelForm):
#     class Meta:
#         model = qr
#         fields = ['template']
