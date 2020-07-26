# Generated by Django 2.2 on 2020-07-01 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ace_it_test_prep', '0014_auto_20200630_1623'),
    ]

    operations = [
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, choices=[('math_2', 'math_2'), ('verbal', 'verbal'), ('math_1', 'math_1'), ('reading', 'reading')], max_length=4, null=True)),
                ('num_questions', models.IntegerField()),
                ('time_limit', models.IntegerField()),
                ('test_type', models.CharField(blank=True, choices=[('act', 'ACT'), ('ssat', 'SSAT'), ('sat', 'SAT')], max_length=4, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='diagram_src',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='section',
            field=models.CharField(blank=True, choices=[('math_2', 'math_2'), ('verbal', 'verbal'), ('math_1', 'math_1'), ('reading', 'reading')], max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='test',
            name='test_type',
            field=models.CharField(blank=True, choices=[('act', 'ACT'), ('ssat', 'SSAT'), ('sat', 'SAT')], max_length=4, null=True),
        ),
    ]
