# Generated by Django 4.2.2 on 2023-06-16 04:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0010_question_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='testing',
            name='is_correct',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='testing',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='testing',
            name='user_answer',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]