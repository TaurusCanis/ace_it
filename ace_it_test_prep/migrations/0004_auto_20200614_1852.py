# Generated by Django 2.2 on 2020-06-14 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ace_it_test_prep', '0003_auto_20200614_1852'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='passage',
        ),
        migrations.AlterField(
            model_name='test',
            name='test_type',
            field=models.CharField(blank=True, choices=[('act', 'ACT'), ('ssat', 'SSAT'), ('sat', 'SAT')], max_length=4, null=True),
        ),
    ]
