# Generated by Django 3.2.16 on 2023-04-29 13:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("buyandsell", "0002_auto_20230428_2306"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="product_image",
            field=models.URLField(blank=True, null=True),
        ),
    ]