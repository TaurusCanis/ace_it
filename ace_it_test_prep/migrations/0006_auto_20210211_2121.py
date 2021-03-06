# Generated by Django 2.2 on 2021-02-11 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ace_it_test_prep', '0005_auto_20210211_2120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='practicetestsectionscore',
            name='section',
            field=models.CharField(choices=[('verbal', 'verbal'), ('math_1', 'math_1'), ('math_2', 'math_2'), ('reading', 'reading')], max_length=14),
        ),
        migrations.AlterField(
            model_name='question',
            name='section',
            field=models.CharField(blank=True, choices=[('verbal', 'verbal'), ('math_1', 'math_1'), ('math_2', 'math_2'), ('reading', 'reading')], max_length=14, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='prep_for_test_type',
            field=models.CharField(blank=True, choices=[('sat', 'SAT'), ('ssat', 'SSAT'), ('act', 'ACT')], max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='test',
            name='test_type',
            field=models.CharField(blank=True, choices=[('sat', 'SAT'), ('ssat', 'SSAT'), ('act', 'ACT')], max_length=4, null=True),
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
            field=models.CharField(blank=True, choices=[('student', 'student'), ('instructor', 'instructor'), ('parent', 'parent')], max_length=14),
        ),
    ]
