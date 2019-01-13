# Generated by Django 2.0 on 2019-01-10 18:24

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.TextField()),
                ('type', models.TextField(blank=True, choices=[('Range', 'Range'), ('Percentage', 'Percentage'), ('Normal', 'Normal')], default=('Normal', 'Normal'), null=True)),
            ],
        ),
        migrations.CreateModel(
            name='QuestionOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField(blank=True, null=True)),
                ('option', models.TextField(blank=True, null=True)),
                ('percentage', models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='options', to='voting.Question')),
            ],
        ),
        migrations.CreateModel(
            name='Voting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('desc', models.TextField(blank=True, null=True)),
                ('start_date', models.DateTimeField(blank=True, null=True)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('gender', models.TextField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], null=True)),
                ('min_age', models.IntegerField(blank=True, null=True)),
                ('max_age', models.IntegerField(blank=True, null=True)),
                ('custom_url', models.CharField(blank=True, max_length=100)),
                ('public_voting', models.BooleanField(default=False)),
                ('tally', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('postproc', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('auths', models.ManyToManyField(related_name='votings', to='base.Auth')),
                ('pub_key', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='voting', to='base.Key')),
                ('question', models.ManyToManyField(related_name='voting_questions', to='voting.Question')),
            ],
        ),
    ]
