# Generated by Django 2.2 on 2021-02-18 20:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('question_maker', '0003_synonym_synonymansweroption'),
    ]

    operations = [
        migrations.AddField(
            model_name='synonymansweroption',
            name='definition',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='question_maker.Definition'),
        ),
    ]