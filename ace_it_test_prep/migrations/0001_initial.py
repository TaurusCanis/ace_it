# Generated by Django 2.2 on 2020-11-20 23:19

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
            name='Instructor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='PracticeExercise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exercise_type', models.CharField(choices=[('practice_test', 'practice_exercise')], max_length=40)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section', models.CharField(blank=True, choices=[('math_2', 'math_2'), ('verbal', 'verbal'), ('reading', 'reading'), ('math_1', 'math_1')], max_length=14, null=True)),
                ('question_text', models.CharField(max_length=1000)),
                ('correct_answer', models.CharField(max_length=10)),
                ('question_type', models.CharField(blank=True, max_length=100, null=True)),
                ('difficulty', models.CharField(blank=True, max_length=100, null=True)),
                ('primary_topic', models.CharField(blank=True, max_length=100, null=True)),
                ('secondary_topic', models.CharField(blank=True, max_length=100, null=True)),
                ('number', models.IntegerField()),
                ('diagram_src', models.CharField(blank=True, max_length=2000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_type', models.CharField(blank=True, choices=[('act', 'ACT'), ('sat', 'SAT'), ('ssat', 'SSAT')], max_length=4, null=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='VocabularyCentralIdea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idea_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='VocabularyRoot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('root_type', models.CharField(choices=[('P', 'Prefix'), ('R', 'Root'), ('S', 'Suffix')], max_length=1)),
                ('term', models.CharField(max_length=100)),
                ('definition', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='VocabularyTerm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('term', models.CharField(max_length=100)),
                ('part_of_speech', models.CharField(blank=True, max_length=20)),
                ('synonyms_list', models.CharField(blank=True, max_length=200)),
                ('definition', models.CharField(blank=True, max_length=500)),
                ('example', models.CharField(blank=True, max_length=1000)),
                ('vocabulary_central_idea', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ace_it_test_prep.VocabularyCentralIdea')),
                ('vocabulary_root', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ace_it_test_prep.VocabularyRoot')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_type', models.CharField(blank=True, choices=[('parent', 'parent'), ('student', 'student'), ('instructor', 'instructor')], max_length=14)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TestSession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_responses_have_been_created', models.BooleanField(default=False)),
                ('started', models.BooleanField(default=False)),
                ('finished', models.BooleanField(default=False)),
                ('section_status_math_1', models.CharField(choices=[('C', 'Completed'), ('I', 'In Progress'), ('N', 'Not Started')], default='N', max_length=1)),
                ('section_status_reading', models.CharField(choices=[('C', 'Completed'), ('I', 'In Progress'), ('N', 'Not Started')], default='N', max_length=1)),
                ('section_status_verbal', models.CharField(choices=[('C', 'Completed'), ('I', 'In Progress'), ('N', 'Not Started')], default='N', max_length=1)),
                ('section_status_math_2', models.CharField(choices=[('C', 'Completed'), ('I', 'In Progress'), ('N', 'Not Started')], default='N', max_length=1)),
                ('time_started_math_1', models.DateTimeField(blank=True, null=True)),
                ('time_finished_math_1', models.DateTimeField(blank=True, null=True)),
                ('time_started_reading', models.DateTimeField(blank=True, null=True)),
                ('time_finished_reading', models.DateTimeField(blank=True, null=True)),
                ('time_started_verbal', models.DateTimeField(blank=True, null=True)),
                ('time_finished_verbal', models.DateTimeField(blank=True, null=True)),
                ('time_started_math_2', models.DateTimeField(blank=True, null=True)),
                ('time_finished_math_2', models.DateTimeField(blank=True, null=True)),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ace_it_test_prep.Test')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TestResponse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('response', models.IntegerField(default=-1)),
                ('answered', models.BooleanField(default=False)),
                ('correct', models.BooleanField(default=False)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ace_it_test_prep.Question')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ace_it_test_prep.TestSession')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prep_for_test_type', models.CharField(blank=True, choices=[('act', 'ACT'), ('sat', 'SAT'), ('ssat', 'SSAT')], max_length=4, null=True)),
                ('instructor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ace_it_test_prep.Instructor')),
                ('user_profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='ace_it_test_prep.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='ReadingPassage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=10000)),
                ('passage_index', models.IntegerField()),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ace_it_test_prep.Test')),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='passage',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ace_it_test_prep.ReadingPassage'),
        ),
        migrations.AddField(
            model_name='question',
            name='practice_exercise',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ace_it_test_prep.PracticeExercise'),
        ),
        migrations.AddField(
            model_name='question',
            name='test',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ace_it_test_prep.Test'),
        ),
        migrations.CreateModel(
            name='PracticeTestSectionScore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section', models.CharField(choices=[('math_2', 'math_2'), ('verbal', 'verbal'), ('reading', 'reading'), ('math_1', 'math_1')], max_length=14)),
                ('num_correct', models.IntegerField()),
                ('num_incorrect', models.IntegerField()),
                ('num_omitted', models.IntegerField()),
                ('raw_score', models.IntegerField()),
                ('test_session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ace_it_test_prep.TestSession')),
            ],
        ),
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='ace_it_test_prep.UserProfile')),
            ],
        ),
        migrations.AddField(
            model_name='instructor',
            name='user_profile',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='ace_it_test_prep.UserProfile'),
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField()),
                ('option', models.CharField(max_length=500)),
                ('explanation', models.CharField(blank=True, default='n', max_length=2000, null=True)),
                ('num_students_choice', models.IntegerField(blank=True, null=True)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ace_it_test_prep.Question')),
            ],
        ),
    ]
