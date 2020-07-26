# Generated by Django 2.2 on 2020-06-27 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ace_it_test_prep', '0009_auto_20200619_0007'),
    ]

    operations = [
        migrations.CreateModel(
            name='VocabularyTerm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('term', models.CharField(max_length=100)),
                ('part_of_speech', models.CharField(max_length=20)),
                ('synonyms_list', models.CharField(max_length=200)),
                ('definition', models.CharField(max_length=500)),
                ('example', models.CharField(max_length=1000)),
            ],
        ),
        migrations.AlterField(
            model_name='test',
            name='test_type',
            field=models.CharField(blank=True, choices=[('sat', 'SAT'), ('act', 'ACT'), ('ssat', 'SSAT')], max_length=4, null=True),
        ),
    ]
