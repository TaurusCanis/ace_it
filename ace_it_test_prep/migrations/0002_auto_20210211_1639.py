# Generated by Django 2.2 on 2021-02-11 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ace_it_test_prep', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='practicetestsectionscore',
            name='section',
            field=models.CharField(choices=[('verbal', 'verbal'), ('math_1', 'math_1'), ('reading', 'reading'), ('math_2', 'math_2')], max_length=14),
        ),
        migrations.AlterField(
            model_name='question',
            name='section',
            field=models.CharField(blank=True, choices=[('verbal', 'verbal'), ('math_1', 'math_1'), ('reading', 'reading'), ('math_2', 'math_2')], max_length=14, null=True),
        ),
        migrations.AlterField(
            model_name='testsession',
            name='section_status_math_1',
            field=models.CharField(choices=[('C', 'Completed'), ('N', 'Not Started'), ('I', 'In Progress')], default='N', max_length=1),
        ),
        migrations.AlterField(
            model_name='testsession',
            name='section_status_math_2',
            field=models.CharField(choices=[('C', 'Completed'), ('N', 'Not Started'), ('I', 'In Progress')], default='N', max_length=1),
        ),
        migrations.AlterField(
            model_name='testsession',
            name='section_status_reading',
            field=models.CharField(choices=[('C', 'Completed'), ('N', 'Not Started'), ('I', 'In Progress')], default='N', max_length=1),
        ),
        migrations.AlterField(
            model_name='testsession',
            name='section_status_verbal',
            field=models.CharField(choices=[('C', 'Completed'), ('N', 'Not Started'), ('I', 'In Progress')], default='N', max_length=1),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user_type',
            field=models.CharField(blank=True, choices=[('instructor', 'instructor'), ('student', 'student'), ('parent', 'parent')], max_length=14),
        ),
    ]
