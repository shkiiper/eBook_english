# Generated by Django 4.2.2 on 2023-06-15 16:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testing', '0016_remove_answerstatistic_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testtype',
            name='correct_answer',
        ),
        migrations.RemoveField(
            model_name='testtype',
            name='question',
        ),
        migrations.RemoveField(
            model_name='testtype',
            name='result',
        ),
        migrations.RemoveField(
            model_name='testtype',
            name='wrong_answer_1',
        ),
        migrations.RemoveField(
            model_name='testtype',
            name='wrong_answer_2',
        ),
        migrations.RemoveField(
            model_name='testtype',
            name='wrong_answer_3',
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('correct_answer', models.CharField(max_length=255)),
                ('wrong_answer_1', models.CharField(max_length=255)),
                ('wrong_answer_2', models.CharField(max_length=255)),
                ('wrong_answer_3', models.CharField(max_length=255)),
                ('result', models.BooleanField(default=False)),
                ('test_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testing.testtype')),
            ],
        ),
    ]