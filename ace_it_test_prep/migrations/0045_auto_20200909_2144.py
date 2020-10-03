# Generated by Django 2.2 on 2020-09-09 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ace_it_test_prep', '0044_auto_20200909_2140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='section',
            field=models.CharField(blank=True, choices=[('math_1', 'math_1'), ('verbal', 'verbal'), ('math_2', 'math_2'), ('reading', 'reading')], max_length=14, null=True),
        ),
        migrations.AlterField(
            model_name='section',
            name='name',
            field=models.CharField(blank=True, choices=[('math_1', 'math_1'), ('verbal', 'verbal'), ('math_2', 'math_2'), ('reading', 'reading')], max_length=14, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user_type',
            field=models.CharField(blank=True, choices=[('parent', 'parent'), ('student', 'student'), ('instructor', 'instructor')], max_length=14),
        ),
    ]