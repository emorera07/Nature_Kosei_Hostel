# Generated by Django 3.1.1 on 2021-06-07 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AppointmentsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=50)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('room_type', models.TextField()),
            ],
        ),
    ]