# Generated by Django 2.0 on 2019-01-07 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0008_merge_20190102_1703'),
    ]

    operations = [
        migrations.AddField(
            model_name='voting',
            name='type',
            field=models.TextField(blank=True, choices=[('Normal', 'Normal'), ('Range', 'Range'), ('Percentage', 'Percentage')], null=True),
        ),
    ]