# Generated by Django 4.2.2 on 2023-06-15 07:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testing', '0012_rename_option3_testalphabet_answer_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='completedtest',
            name='test_alphabet',
            field=models.ForeignKey(blank=True, default=0, null=True, on_delete=django.db.models.deletion.CASCADE, to='testing.testalphabet'),
        ),
        migrations.AlterField(
            model_name='completedtest',
            name='test_family_friends',
            field=models.ForeignKey(blank=True, default=0, null=True, on_delete=django.db.models.deletion.CASCADE, to='testing.testfamilyfriends'),
        ),
        migrations.AlterField(
            model_name='completedtest',
            name='test_food_drinks',
            field=models.ForeignKey(blank=True, default=0, null=True, on_delete=django.db.models.deletion.CASCADE, to='testing.testfooddrinks'),
        ),
        migrations.AlterField(
            model_name='completedtest',
            name='test_numbers',
            field=models.ForeignKey(blank=True, default=0, null=True, on_delete=django.db.models.deletion.CASCADE, to='testing.testnumbers'),
        ),
    ]
