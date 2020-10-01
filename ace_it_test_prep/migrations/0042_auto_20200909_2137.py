# Generated by Django 2.2 on 2020-09-09 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ace_it_test_prep', '0041_auto_20200726_1526'),
    ]

    operations = [
        migrations.CreateModel(
            name='VocabularySet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='VocuabularyRoot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('root_type', models.CharField(choices=[('P', 'Prefix'), ('R', 'Root'), ('S', 'Sufix')], max_length=1)),
                ('term', models.CharField(max_length=100)),
                ('definition', models.CharField(max_length=1000)),
            ],
        ),
        migrations.AlterField(
            model_name='question',
            name='section',
            field=models.CharField(blank=True, choices=[('reading', 'reading'), ('verbal', 'verbal'), ('math_2', 'math_2'), ('math_1', 'math_1')], max_length=14, null=True),
        ),
        migrations.AlterField(
            model_name='section',
            name='name',
            field=models.CharField(blank=True, choices=[('reading', 'reading'), ('verbal', 'verbal'), ('math_2', 'math_2'), ('math_1', 'math_1')], max_length=14, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user_type',
            field=models.CharField(blank=True, choices=[('parent', 'parent'), ('student', 'student'), ('instructor', 'instructor')], max_length=14),
        ),
    ]
