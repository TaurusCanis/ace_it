# Generated by Django 2.2 on 2021-02-13 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ace_it_test_prep', '0009_auto_20210212_2204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='practicetestsectionscore',
            name='section',
            field=models.CharField(choices=[('reading', 'reading'), ('math_2', 'math_2'), ('verbal', 'verbal'), ('math_1', 'math_1')], max_length=14),
        ),
        migrations.AlterField(
            model_name='question',
            name='section',
            field=models.CharField(blank=True, choices=[('reading', 'reading'), ('math_2', 'math_2'), ('verbal', 'verbal'), ('math_1', 'math_1')], max_length=14, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='prep_for_test_type',
            field=models.CharField(blank=True, choices=[('sat', 'SAT'), ('act', 'ACT'), ('ssat', 'SSAT')], max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='test',
            name='test_type',
            field=models.CharField(blank=True, choices=[('sat', 'SAT'), ('act', 'ACT'), ('ssat', 'SSAT')], max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='testsession',
            name='section_status_math_1',
            field=models.CharField(choices=[('I', 'In Progress'), ('N', 'Not Started'), ('C', 'Completed')], default='N', max_length=1),
        ),
        migrations.AlterField(
            model_name='testsession',
            name='section_status_math_2',
            field=models.CharField(choices=[('I', 'In Progress'), ('N', 'Not Started'), ('C', 'Completed')], default='N', max_length=1),
        ),
        migrations.AlterField(
            model_name='testsession',
            name='section_status_reading',
            field=models.CharField(choices=[('I', 'In Progress'), ('N', 'Not Started'), ('C', 'Completed')], default='N', max_length=1),
        ),
        migrations.AlterField(
            model_name='testsession',
            name='section_status_verbal',
            field=models.CharField(choices=[('I', 'In Progress'), ('N', 'Not Started'), ('C', 'Completed')], default='N', max_length=1),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user_type',
            field=models.CharField(blank=True, choices=[('parent', 'parent'), ('instructor', 'instructor'), ('student', 'student')], max_length=14),
        ),
    ]
