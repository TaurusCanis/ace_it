# Generated by Django 2.2 on 2020-06-27 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ace_it_test_prep', '0011_auto_20200627_1837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='test_type',
            field=models.CharField(blank=True, choices=[('sat', 'SAT'), ('ssat', 'SSAT'), ('act', 'ACT')], max_length=4, null=True),
        ),
    ]
