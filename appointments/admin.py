from django.contrib import admin

# Register your models here.
from appointments.models import Event

admin.site.register(Event)
