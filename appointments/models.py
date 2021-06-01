from django.db import models

# Create your models here.
class AppointmentsModel(models.Model):
    user = models.CharField(max_length=50)
    date = models.DateTimeField(input_formats=['%d/%m/%Y %H:%M'])
    def __str__(self): #Devuelve etiqueta del objeto
        return '{}{}'.format(self.user, self.date)
