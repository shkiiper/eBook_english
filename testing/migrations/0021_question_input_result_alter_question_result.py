# Generated by Django 4.2.2 on 2023-06-15 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testing', '0020_alter_question_result'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='input_result',
            field=models.CharField(default=0, max_length=255),
        ),
        migrations.AlterField(
            model_name='question',
            name='result',
            field=models.CharField(default=0, max_length=255),
        ),
    ]