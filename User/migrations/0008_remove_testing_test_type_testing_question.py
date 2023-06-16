# Generated by Django 4.2.2 on 2023-06-15 21:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0007_remove_testtype_level_question_level'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testing',
            name='test_type',
        ),
        migrations.AddField(
            model_name='testing',
            name='question',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='User.question'),
        ),
    ]