# Generated by Django 2.2 on 2021-02-11 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ace_it_test_prep', '0003_auto_20210211_1814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testsession',
            name='section_status_math_1',
            field=models.CharField(choices=[('N', 'Not Started'), ('I', 'In Progress'), ('C', 'Completed')], default='N', max_length=1),
        ),
        migrations.AlterField(
            model_name='testsession',
            name='section_status_math_2',
            field=models.CharField(choices=[('N', 'Not Started'), ('I', 'In Progress'), ('C', 'Completed')], default='N', max_length=1),
        ),
        migrations.AlterField(
            model_name='testsession',
            name='section_status_reading',
            field=models.CharField(choices=[('N', 'Not Started'), ('I', 'In Progress'), ('C', 'Completed')], default='N', max_length=1),
        ),
        migrations.AlterField(
            model_name='testsession',
            name='section_status_verbal',
            field=models.CharField(choices=[('N', 'Not Started'), ('I', 'In Progress'), ('C', 'Completed')], default='N', max_length=1),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user_type',
            field=models.CharField(blank=True, choices=[('parent', 'parent'), ('instructor', 'instructor'), ('student', 'student')], max_length=14),
        ),
    ]
