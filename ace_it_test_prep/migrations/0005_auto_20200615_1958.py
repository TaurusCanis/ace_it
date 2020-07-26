# Generated by Django 2.2 on 2020-06-15 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ace_it_test_prep', '0004_auto_20200614_1852'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='option_a',
            field=models.CharField(default='A', max_length=100),
        ),
        migrations.AddField(
            model_name='question',
            name='option_b',
            field=models.CharField(default='B', max_length=100),
        ),
        migrations.AddField(
            model_name='question',
            name='option_c',
            field=models.CharField(default='C', max_length=100),
        ),
        migrations.AddField(
            model_name='question',
            name='option_d',
            field=models.CharField(default='D', max_length=100),
        ),
        migrations.AddField(
            model_name='question',
            name='option_e',
            field=models.CharField(blank=True, default='E', max_length=100, null=True),
        ),
        migrations.DeleteModel(
            name='AnswerOptions',
        ),
    ]
