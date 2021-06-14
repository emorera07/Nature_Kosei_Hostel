from django.db import models

# Create your models here.

class Event(models.Model):
    user = models.CharField(max_length=200)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    def __str__(self):#Devuelve la etiqueta
        return '{}{}{}'.format(self.user, self.start_time, self.end_time)
