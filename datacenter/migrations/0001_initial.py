# Generated by Django 3.2.15 on 2022-08-14 21:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Passcard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('passcode', models.CharField(max_length=200, unique=True)),
                ('owner_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('entered_at', models.DateTimeField()),
                ('leaved_at', models.DateTimeField(null=True)),
                ('passcard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datacenter.passcard')),
            ],
        ),
    ]