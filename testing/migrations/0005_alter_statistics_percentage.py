# Generated by Django 4.2.2 on 2023-06-15 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testing', '0004_remove_experiencepoints_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statistics',
            name='percentage',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
    ]
