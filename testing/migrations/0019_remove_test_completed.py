# Generated by Django 4.2.2 on 2023-06-15 17:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testing', '0018_test_completed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='test',
            name='completed',
        ),
    ]