# Generated by Django 2.2 on 2020-07-16 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ace_it_test_prep', '0031_auto_20200709_1740'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='primary_topic',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='secondary_topic',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='section',
            field=models.CharField(blank=True, choices=[('reading', 'reading'), ('math_2', 'math_2'), ('math_1', 'math_1'), ('verbal', 'verbal')], max_length=14, null=True),
        ),
        migrations.AlterField(
            model_name='section',
            name='name',
            field=models.CharField(blank=True, choices=[('reading', 'reading'), ('math_2', 'math_2'), ('math_1', 'math_1'), ('verbal', 'verbal')], max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='section',
            name='test_type',
            field=models.CharField(blank=True, choices=[('sat', 'SAT'), ('ssat', 'SSAT'), ('act', 'ACT')], max_length=4, null=True),
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
    ]
