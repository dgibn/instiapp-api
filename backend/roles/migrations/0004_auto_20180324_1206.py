# Generated by Django 2.0.2 on 2018-03-24 06:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('roles', '0003_auto_20180320_2314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bodyrole',
            name='body',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='roles', to='bodies.Body'),
        ),
    ]
