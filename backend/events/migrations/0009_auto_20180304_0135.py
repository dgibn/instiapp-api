# Generated by Django 2.0.2 on 2018-03-03 20:05

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0008_auto_20180303_1640'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='followers',
        ),
        migrations.AlterField(
            model_name='usereventstatus',
            name='event',
            field=models.ForeignKey(default=uuid.uuid4, on_delete=django.db.models.deletion.CASCADE, related_name='user_event_statuses', to='events.Event'),
        ),
        migrations.AlterField(
            model_name='usereventstatus',
            name='user',
            field=models.ForeignKey(default=uuid.uuid4, on_delete=django.db.models.deletion.CASCADE, related_name='events_followed', to='users.UserProfile'),
        ),
    ]