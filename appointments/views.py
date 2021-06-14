"""
    Reference https://github.com/catafest/django_test_002/tree/master/test_calendar/first_calendar
"""
from django.shortcuts import render
from django.shortcuts import reverse
from django.http import HttpResponse
from django.http import HttpResponseRedirect
# import next python packages
from datetime import datetime
from django.views import generic
from django.utils.safestring import mark_safe
from .models import *
from .forms import EventForm
from .class_calendar import Calendar
from .urls import *

# Create a class for calendar
class CalendarView(generic.ListView):
    model = Event
    template_name = 'calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # use today's date for the calendar
        d = get_date(self.request.GET.get('day', None))

        # Instantiate our calendar class with today's year and date
        cal = Calendar(d.year, d.month)

        # Call the formatmonth method, which returns our calendar as a table
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        return context

def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()

def NewAppointmentsView(request, event_id=None):
    instance = Event()
    if event_id:
        instance = get_object_or_404(Event, pk=event_id)
    else:
        instance = Event()

    form = EventForm(request.POST or None, instance=instance)
    if request.POST and form.is_valid():
        form.save()
        return render(request, 'home_page.html')
    else:
        return render(request, 'NewAppointments.html', {'form': form})

def EditAppointmentsView(request, event_id=None):
    instance = Event()
    if event_id:
        instance = get_object_or_404(Event, pk=event_id)
    else:
        instance = Event()
    if request.POST and form.is_valid():
        form = EventForm(request.POST, instance=instance)
        instance = form.save(commit=False)
        instance.user = request.user
        if instance.start_time == request.start_time:
            form.objects.start_time.delete()
        if instance.end_time == request.end_time:
            form.objects.end_time.delete()
        form.objects.user.delete()
        Event.objects.all().delete()
        Event.save()
        return render(request, 'home_page.html')
    else:
        return render(request, 'NewAppointments.html', {'form': form})
