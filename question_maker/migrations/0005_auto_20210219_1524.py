# Generated by Django 2.2 on 2021-02-19 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question_maker', '0004_synonymansweroption_definition'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='synonymansweroption',
            name='has_been_vetted',
        ),
        migrations.AddField(
            model_name='synonym',
            name='has_been_vetted',
            field=models.BooleanField(default=False),
        ),
    ]
