# Generated by Django 4.2.2 on 2023-06-14 18:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('testing', '0002_testgenerator_testalphabet_result_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompletedTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_type', models.CharField(max_length=100)),
                ('total_questions', models.IntegerField(default=0)),
                ('total_correct_answers', models.IntegerField(default=0)),
                ('completion_date', models.DateField(auto_now_add=True)),
                ('difficulty_level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testing.difficultylevel')),
                ('test_alphabet', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='testing.testalphabet')),
                ('test_family_friends', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='testing.testfamilyfriends')),
                ('test_food_drinks', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='testing.testfooddrinks')),
                ('test_numbers', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='testing.testnumbers')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='TestGenerator',
        ),
    ]