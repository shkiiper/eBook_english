# Generated by Django 4.2.2 on 2023-06-15 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testing', '0014_answerstatistic_score_test_testtype_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='testtype',
            name='question',
            field=models.CharField(default='question', max_length=50),
        ),
    ]
