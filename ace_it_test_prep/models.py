from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

# User = get_user_model()

TEST_TYPES = {
    ("ssat", "SSAT"), ("sat", "SAT"), ("act", "ACT")
}

SECTION_TYPES = {
    ("math_1", "math_1"), ("math_2", "math_2"), ("reading", "reading"), ("verbal", "verbal")
}

USER_TYPES = {
    ("student", "student"), ("instructor", "instructor"), ("parent", "parent")
}

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(choices=USER_TYPES, max_length=14, blank=True)

class Student(models.Model):
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    prep_for_test_type = models.CharField(choices=TEST_TYPES, max_length=4, blank=True, null=True)
    instructor = models.ForeignKey("Instructor", on_delete=models.CASCADE, null=True)

class Instructor(models.Model):
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)

class Parent(models.Model):
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)

class Test(models.Model):
    test_type = models.CharField(choices=TEST_TYPES, max_length=4, blank=True, null=True)
    name = models.CharField(max_length=200)

class TestSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    started = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)

    # def __str__(self):
        # return test.name

class Assignment(models.Model):
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    date_assigned = models.DateTimeField(auto_now_add=True)
    ##This should probably be changed to allow for future assignments ##
    due_date = models.DateTimeField(null=True, blank=True)
    started = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)

class AssignmentSession(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    test_session = models.ForeignKey(TestSession, on_delete=models.CASCADE)

class Section(models.Model):
    name = models.CharField(choices=SECTION_TYPES, max_length=14, blank=True, null=True)
    num_questions = models.IntegerField()
    time_limit = models.IntegerField()
    test_type = models.CharField(choices=TEST_TYPES, max_length=14, blank=True, null=True)
    rank = models.IntegerField()

    def __str__(self):
        return self.name

class TestSessionSection(models.Model):
    test_session = models.ForeignKey(TestSession, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    started = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.test_session.test.test_type + " - " + self.section.name


# class SCAT(models.Model):
#     math = models.ForeignKey(SCATMath, on_delete=models.CASCADE)
#     verbal = models.ForeignKey(SCATVerbal, on_delete=models.CASCADE)
#
# class SCATVerbal(models.Model):
#     test = models.ForeignKey(SSAT, on_delete=models.CASCADE)
#     question = models.CharField()
#     passage = models.ForeignKey(ReadingPassage, on_delete=models.CASCADE)
#     question_type = models.CharField()
#     difficulty = models.CharField()
#
# class SCATMath(models.Model):
#     test = models.ForeignKey(SSAT, on_delete=models.CASCADE)
#     question = models.CharField()
#     passage = models.ForeignKey(ReadingPassage, on_delete=models.CASCADE)
#     question_type = models.CharField()
#     difficulty = models.CharField()

class SSAT(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    math_1_start_time = models.DateTimeField()
    math_1_end_time = models.DateTimeField()
    math_2_start_time = models.DateTimeField()
    math_2_end_time = models.DateTimeField()
    reading_start_time = models.DateTimeField()
    reading_end_time = models.DateTimeField()
    verbal_start_time = models.DateTimeField()
    verbal_end_time = models.DateTimeField()

class SSATReadingQuestion(models.Model):
    test = models.ForeignKey(SSAT, on_delete=models.CASCADE)
    question = models.CharField(max_length=10000)
    passage = models.ForeignKey("ReadingPassage", on_delete=models.CASCADE)
    question_type = models.CharField(max_length=1000)
    difficulty = models.CharField(max_length=100)

class ReadingPassage(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    text = models.CharField(max_length=10000)
    passage_index = models.IntegerField()

class SSATVerbalQuestion(models.Model):
    test = models.ForeignKey(SSAT, on_delete=models.CASCADE)
    question = models.CharField(max_length=1000)
    passage = models.ForeignKey(ReadingPassage, on_delete=models.CASCADE)
    concept = models.CharField(max_length=100)
    difficulty = models.CharField(max_length=10)

class SSATMathQuestion(models.Model):
    test = models.ForeignKey(SSAT, on_delete=models.CASCADE)
    question = models.CharField(max_length=1000)
    diagram = models.ImageField(blank=True, null=True)
    concept = models.CharField(max_length=100)
    difficulty = models.CharField(max_length=10)

class QCMathQuestion(models.Model):
    test = models.ForeignKey(SSAT, on_delete=models.CASCADE)
    question = models.CharField(max_length=1000)
    passage = models.ForeignKey(ReadingPassage, on_delete=models.CASCADE)
    question_type = models.CharField(max_length=100)
    difficulty = models.CharField(max_length=10)

class Question(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    section = models.CharField(choices=SECTION_TYPES, max_length=14, blank=True, null=True)
    question_text = models.CharField(max_length=1000)
    correct_answer = models.CharField(max_length=10)
    passage = models.ForeignKey(ReadingPassage, on_delete=models.CASCADE, blank=True, null=True)
    question_type = models.CharField(max_length=100, blank=True, null=True)
    difficulty = models.CharField(max_length=100, blank=True, null=True)
    primary_topic = models.CharField(max_length=100, blank=True, null=True)
    secondary_topic = models.CharField(max_length=100, blank=True, null=True)
    number = models.IntegerField()
    diagram_src = models.CharField(max_length=2000, blank=True, null=True)
    # option_a = models.CharField(max_length=100, default="A")
    # option_b = models.CharField(max_length=100, default="B")
    # option_c = models.CharField(max_length=100, default="C")
    # option_d = models.CharField(max_length=100, default="D")
    # option_e = models.CharField(max_length=100, default="E", null=True, blank=True)

class Answer(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE, blank=False)
	# LABEL = [('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')]
	# label = models.CharField(choices=LABEL, max_length=200, default='A')
	value = models.IntegerField()
	option = models.CharField(max_length = 500)
	explanation = models.CharField(max_length=2000, default='n', blank=True, null=True)
	num_students_choice = models.IntegerField(blank=True, null=True)

class TestResponse(models.Model):
	session = models.ForeignKey(TestSession, on_delete=models.CASCADE, blank=False)
	question = models.ForeignKey(Question, on_delete=models.CASCADE, blank=False)
	# test_id = models.ForeignKey(Test, on_delete=models.CASCADE, default='1')
	# SECTION = [('math_1', 'MATH_1'), ('reading', 'READING'), ('verbal', 'VERBAL'), ('math_2', 'MATH_2')]
	# section = models.CharField(choices=SECTION, max_length=200)
#	number = models.CharField(max_length=200)
#	question = models.CharField(max_length=200)
	response = models.IntegerField(default=-1)
	answered = models.BooleanField(default=False)
	correct = models.BooleanField(default=False)

class VocabularyTerm(models.Model):
    term = models.CharField(max_length=100)
    part_of_speech = models.CharField(max_length=20, blank=True)
    synonyms_list = models.CharField(max_length=200, blank=True)
    vocabulary_root = models.ForeignKey("VocabularyRoot", on_delete=models.CASCADE, blank=True, null=True)
    vocabulary_central_idea = models.ForeignKey("VocabularyCentralIdea", on_delete=models.CASCADE, blank=True, null=True)
    definition = models.CharField(max_length=500, blank=True)
    example = models.CharField(max_length=1000, blank=True)

    def __str__(self):
        return self.term

class VocabularySet(models.Model):
    source = models.CharField(max_length=100)

class VocabularyRoot(models.Model):
    root_type = models.CharField(choices=[("P", "Prefix"), ("R", "Root"), ("S", "Suffix")], max_length=1)
    term = models.CharField(max_length=100)
    definition = models.CharField(max_length=1000)

    def __str__(self):
        return self.term

class VocabularyTermSynonym(models.Model):
    term = models.ForeignKey(VocabularyTerm, on_delete=models.CASCADE)
    option_a = models.CharField(max_length=100)
    option_b = models.CharField(max_length=100)
    option_c = models.CharField(max_length=100)
    option_d = models.CharField(max_length=100)
    option_e = models.CharField(max_length=100, blank=True, null=True)
    correct_answer = models.CharField(max_length=100)

    def __str__(self):
        return self.term.term

    def natural_key(self):
        return self.term.term

class PracticeSet(models.Model):
    section = models.CharField(max_length=200)
    sub_section = models.CharField(max_length=200)
    sub_section_category = models.CharField(max_length=200)

class PracticeSetQuestion(models.Model):
    question = models.CharField(max_length=10000)
    diagram = models.CharField(max_length=10000, blank=True, null=True)
    passage = models.CharField(max_length=10000, blank=True, null=True)
    extra_info_text = models.CharField(max_length=10000, blank=True, null=True)
    option_a = models.CharField(max_length=300)
    option_b = models.CharField(max_length=300)
    option_c = models.CharField(max_length=300)
    option_d = models.CharField(max_length=300)
    option_e = models.CharField(max_length=300, blank=True, null=True)
    correct_answer = models.CharField(max_length=300)
    category_1 = models.CharField(max_length=300)
    category_2 = models.CharField(max_length=300)

class VocabularyCentralIdea(models.Model):
    idea_name = models.CharField(max_length=100)

    def __str__(self):
        return self.idea_name
    

