# Generated by Django 4.2.2 on 2023-06-15 04:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testing', '0009_alter_completedtest_test_alphabet_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='completedtest',
            name='test_alphabet',
        ),
        migrations.RemoveField(
            model_name='completedtest',
            name='test_family_friends',
        ),
        migrations.RemoveField(
            model_name='completedtest',
            name='test_food_drinks',
        ),
        migrations.RemoveField(
            model_name='completedtest',
            name='test_numbers',
        ),
    ]
