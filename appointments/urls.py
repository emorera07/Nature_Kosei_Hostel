from django.urls import path

from . import views

urlpatterns = [
    path('', views.CalendarView.as_view(), name='calendar'),
    path('NewAppointments/', views.NewAppointmentsView, name='NewAppointments'),
    path('EditAppointments/', views.NewAppointmentsView, name='EditAppointments'),
]
