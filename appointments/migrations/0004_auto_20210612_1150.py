# Generated by Django 3.1.1 on 2021-06-12 17:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0003_auto_20210608_0916'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='title',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='event',
            name='description',
        ),
    ]
