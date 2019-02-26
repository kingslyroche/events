from django.db import models

# Create your models here.
class Events(models.Model):
    event_id=models.IntegerField()
    event_name=models.CharField(max_length=32)

    def __str__(self):
        return ("{} ({})").format(self.event_name,self.event_id)

class Attendees (models.Model):
   
    first_name=models.CharField(max_length=32)
    last_name=models.CharField(max_length=32)
    events=models.IntegerField()

    def __str__(self):
        return f("{} {}").format(self.first_name,self.last_name)