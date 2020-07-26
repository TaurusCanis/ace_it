# Generated by Django 2.2 on 2020-07-09 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ace_it_test_prep', '0029_auto_20200709_1740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='section',
            field=models.CharField(blank=True, choices=[('reading', 'reading'), ('verbal', 'verbal'), ('math_1', 'math_1'), ('math_2', 'math_2')], max_length=14, null=True),
        ),
        migrations.AlterField(
            model_name='section',
            name='name',
            field=models.CharField(blank=True, choices=[('reading', 'reading'), ('verbal', 'verbal'), ('math_1', 'math_1'), ('math_2', 'math_2')], max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='section',
            name='test_type',
            field=models.CharField(blank=True, choices=[('act', 'ACT'), ('ssat', 'SSAT'), ('sat', 'SAT')], max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='prep_for_test_type',
            field=models.CharField(blank=True, choices=[('act', 'ACT'), ('ssat', 'SSAT'), ('sat', 'SAT')], max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='test',
            name='test_type',
            field=models.CharField(blank=True, choices=[('act', 'ACT'), ('ssat', 'SSAT'), ('sat', 'SAT')], max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user_type',
            field=models.CharField(blank=True, choices=[('s', 'student'), ('p', 'parent'), ('i', 'instructor')], max_length=4),
        ),
    ]
