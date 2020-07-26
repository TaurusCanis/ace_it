# Generated by Django 3.0.5 on 2020-06-13 21:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ReadingPassage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='SSAT',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('math_1_start_time', models.DateTimeField()),
                ('math_1_end_time', models.DateTimeField()),
                ('math_2_start_time', models.DateTimeField()),
                ('math_2_end_time', models.DateTimeField()),
                ('reading_start_time', models.DateTimeField()),
                ('reading_end_time', models.DateTimeField()),
                ('verbal_start_time', models.DateTimeField()),
                ('verbal_end_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_type', models.CharField(blank=True, choices=[('ssat', 'SSAT'), ('act', 'ACT'), ('sat', 'SAT')], max_length=4, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TestSession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ace_it_test_prep.Test')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SSATVerbalQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=1000)),
                ('concept', models.CharField(max_length=100)),
                ('difficulty', models.CharField(max_length=10)),
                ('passage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ace_it_test_prep.ReadingPassage')),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ace_it_test_prep.SSAT')),
            ],
        ),
        migrations.CreateModel(
            name='SSATReadingQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=1000)),
                ('question_type', models.CharField(max_length=100)),
                ('difficulty', models.CharField(max_length=10)),
                ('passage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ace_it_test_prep.ReadingPassage')),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ace_it_test_prep.SSAT')),
            ],
        ),
        migrations.CreateModel(
            name='SSATMathQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=1000)),
                ('diagram', models.ImageField(blank=True, null=True, upload_to='')),
                ('concept', models.CharField(max_length=100)),
                ('difficulty', models.CharField(max_length=10)),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ace_it_test_prep.SSAT')),
            ],
        ),
        migrations.AddField(
            model_name='ssat',
            name='test',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ace_it_test_prep.Test'),
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=1000)),
                ('question_type', models.CharField(max_length=100)),
                ('difficulty', models.CharField(max_length=10)),
                ('passage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ace_it_test_prep.ReadingPassage')),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ace_it_test_prep.SSAT')),
            ],
        ),
        migrations.CreateModel(
            name='QCMathQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=1000)),
                ('question_type', models.CharField(max_length=100)),
                ('difficulty', models.CharField(max_length=10)),
                ('passage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ace_it_test_prep.ReadingPassage')),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ace_it_test_prep.SSAT')),
            ],
        ),
    ]
