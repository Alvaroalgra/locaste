# Generated by Django 2.0 on 2018-12-10 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0003_auto_20180605_0842'),
    ]

    operations = [
        migrations.AddField(
            model_name='voting',
            name='custom_url',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
