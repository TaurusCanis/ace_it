from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import (
    Question, Test, TestSession, TestResponse, Answer, VocabularyTerm, 
    ReadingPassage, Section, TestSessionSection, Student, Parent, 
    Instructor, UserProfile, Assignment, AssignmentSession, 
    VocabularyRoot, VocabularyTermSynonym, 
    VocabularyCentralIdea, PracticeSession, PracticeExercise
)
from .forms import SignUpForm
from django.core import serializers
from django.forms.models import model_to_dict
from django.db.models.query import QuerySet
import json, random
from django.contrib.staticfiles.storage import staticfiles_storage
from django.apps import apps
from django.core import serializers
from django.contrib import messages
from django.views.generic.base import TemplateView, View
from django.views.generic import CreateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.contrib.auth.hashers import make_password
from django.contrib.auth.views import LoginView, LogoutView

# Create your views here.

def save_test_response(request, question_id):
    print("SAVING")
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    question_index = body['index'] + 1
    user_response = body['response']
    session_id = body['session_id']
    question_id = body['question_id']
    session_test_responses = TestResponse.objects.filter(session__id=session_id)
    test_response = TestResponse.objects.get(session__id=session_id, question__id=question_id)
    test_response.response = user_response
    test_response.save()
    question = Question.objects.get(id=question_id)
    return JsonResponse({"message": "success"})

class IndexView(TemplateView):
    template_name = "ace_it_test_prep/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = SignUpForm()
        return context

class SignUpView(CreateView):
    # model = User
    # fields = ['first_name', 'last_name', 'username', 'password', 'email']
    form_class = SignUpForm
    template_name = "ace_it_test_prep/index.html"
    success_url = 'ace_it_test_prep/index.html'

    def form_invalid(self, form):
        print("FORM INVALID: ", form.errors)
        return super().form_invalid(form)

    def form_valid(self,form):
        new_user_data = self.create_new_user(form)
        if new_user_data[0] is not None:
            login(self.request, new_user_data[0])
            url = self.get_success_url()
            return redirect(url)
        else:
            return super().form_invalid(form)

    def get_success_url(self):
        return reverse('ace_it_test_prep:account_home')

    def create_new_user(self, form):
        username=form.cleaned_data['username']
        # email=form.cleaned_data['email']        
        password=form.cleaned_data['password1']
        first_name=form.cleaned_data['first_name']
        last_name=form.cleaned_data['last_name']

        new_user = User.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name)
        new_user.save()

        # self.object = form.save()
        # self.object.set_password(password)
        # self.object.save()

        new_user_profile = self.create_new_user_profile(new_user)
        
        new_student = self.create_new_student(new_user_profile)
        
        user = authenticate(self.request, username=username, password=password)

        return (user, new_user_profile, new_student)

    def create_new_user_profile(self, new_user):
        new_user_profile = UserProfile(user=new_user, user_type="student")
        new_user_profile.save() 
        return new_user_profile

    def create_new_student(self, new_user_profile):
        new_student = Student(user_profile=new_user_profile, prep_for_test_type="ssat")
        new_student.save() 
        return new_student

# class LoginUserView(LoginView):
#     template_name = "ace_it_test_prep/index.html"
#     print("LoginUserView")
#     def get_success_url(self):
#         print("get_success_url*****!!!!!!!@@@@@@@@@")
#         url = 'ace_it_test_prep:account_home'
#         return reverse(url, kwargs={ 'profile_type':  self.get_user_profile_type() })

#     def get_user_profile_type(self):
#         print("get_user_profile_type")
#         user_profile = UserProfile.objects.get(user=self.request.user)
#         profile_type = user_profile.user_type
#         return profile_type
        

def uploads(request):
    return render(request, "ace_it_test_prep/uploads.html")

def upload_TI_Quizlet_Terms(request):

    # json_data = os.path.join(settings.STATIC_ROOT, 'TestInnovatorsQuizlet300.json')
    url = staticfiles_storage.url('TestInnovatorsQuizlet300.json')
    json_data = open(url)
    content = json.loads(json_data.readlines()[0])
    print("content type: ", type(content))
    print("content[0]: ", content[0])
    for entry in content:
        new_vocabulary_item = VocabularyTerm(
            term=entry['word'],
            part_of_speech=entry['part_of_speech'],
            synonyms_list=', '.join(entry['synonyms']),
            example=entry['example']
        )
        # new_vocabulary_item.save()
        print("entry: ", entry['synonyms'])
    vocabulary_terms = VocabularyTerm.objects.all()
    print("vocabulary_terms: ", vocabulary_terms)
    return JsonResponse({"data": content})


# def index(request):
#     print("INDEX PAGE")
#     return render(request, "ace_it_test_prep/index.html")

# def signup(request):
#     first_name = request.POST.get("first_name")
#     last_name = request.POST.get("last_name")
#     username = request.POST.get("username")
#     password = request.POST.get("password")
#     test_selection = request.POST.get("test_selection")
#     prep_for_test_type = request.POST.get("test_selection")
#     user_type = request.POST.get("user_type")

#     try:
#         user = User.objects.create_user(username, username, password, first_name=first_name, last_name=last_name)
#         user_profile = UserProfile.objects.create(user=user, user_type=user_type)

#         if user_type == "student":
#             print("student")
#             new_student_profile = Student.objects.create(user_profile=user_profile, prep_for_test_type=prep_for_test_type)
#             # new_student_profile.prep_for_test_type = prep_for_test_type
#         elif user_type == "parent":
#             print("parent")
#             new_parent_profile = Parent.objects.create(user_profile=user_profile)
#         else:
#             print("instructor")
#             new_instructor_profile = Instructor.objects.create(user_profile=user_profile)

#         login(request, user)

#         profile_type = user_profile.user_type

#         return redirect('ace_it_test_prep:account_home', profile_type=profile_type)
#     # return render(request, "ace_it_test_prep/account_home.html", context)
#     except Exception as e:
#         messages.warning(request, e)
#         return render(request, "ace_it_test_prep/index.html")


def login_user(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    print("username: ", username)
    print("password: ", password)
    print("password: ", make_password(password))
    user = authenticate(request, username=username, password=password)
    print("user!!!!!: ", user)
    
    if user is not None:
        user_profile = UserProfile.objects.get(user=user)
        profile_type = user_profile.user_type
        login(request, user)
        context = {
            "profile_type": profile_type
        }
        
        return redirect('ace_it_test_prep:account_home')
    else:
        messages.warning(request, 'Username and/or password is not correct.')
        return render(request, "ace_it_test_prep/index.html")

def logout_user(request):
    logout(request)
    return render(request, "ace_it_test_prep/index.html")

class AccountDetailView(DetailView):
    template_name = "ace_it_test_prep/account_home.html"
    def get(self, request, *args, **kwargs):
        print("AccountDetailView")
        user_profile = UserProfile.objects.get(user__id=request.user.id)
        if user_profile.user_type == "student":
            student = Student.objects.get(user_profile=user_profile)
            student_tests_completed = TestSession.objects.filter(user=request.user).values_list('test_id', flat=True).order_by('id')
            next_practice_test = Test.objects.exclude(id__in=student_tests_completed).order_by('id').first()
            print("next_practice_test: ", next_practice_test)
            context = {
                "student": student,
                "next_practice_test": next_practice_test
            }
            return render(request, "ace_it_test_prep/account_home.html", context)

class PracticeTestListView(ListView):
    model = Test

class PracticeTestDetailView(DetailView):
    model = Test
    template_name = "ace_it_test_prep/practice_test_detail_view.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        test_session = self.get_test_session()
        context['test_session'] = test_session
        context['section_statuses'] = get_section_statuses(test_session)
        print("CONTEXT: ", context)
        return context

    def get_test_session(self):
        try:
            test_session = TestSession.objects.get(user=self.request.user, test=self.object)
        except:
            test_session = TestSession(user=self.request.user, test=self.object)
            test_session.save()
            print("TESTSESSION: ", test_session)
        return test_session

    # def get_section_statuses(self, *args):
    #     test_session = args[0]
    #     test_session_fields = test_session._meta.fields
    #     statuses = {}
    #     for field in test_session_fields:
    #         if field.name.startswith("section"):
    #             section_name = field.name.replace("section_status_","").replace("_", " ").capitalize()
    #             statuses[section_name] = getattr(test_session, field.name)
    #     return statuses

def get_section_statuses(test_session):
    test_session_fields = test_session._meta.fields
    statuses = {}
    for field in test_session_fields:
        if field.name.startswith("section"):
            section_name = field.name.replace("section_status_","").replace("_", " ").capitalize()
            statuses[section_name] = getattr(test_session, field.name)
    print("Statuses: ", statuses)
    return statuses

# What does this view do????
# I think it was replaced by PracticeTestDetailView
class PracticeTestOverview(TemplateView):
    template_name = "ace_it_test_prep/practice_test_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        practice_test = Test.objects.get(id=kwargs['test_id'])
        test_session = TestSession.objects.filter(user=self.request.user, test=practice_test)
        practice_test_section_statuses = self.get_section_statuses(test_session)
        context['practice_test'] = practice_test
        context['test_session'] = test_session
        context['practice_test_section_statuses'] = practice_test_section_statuses
        return context

    def get_section_statuses(self, test_session):
        test_session_fields = test_session.values()
        section_statuses = []
        for key, value in enumerate(test_session_fields):
            if key.startswith("section"):
                section_statuses.append(key)
        return section_statuses

class PracticeTestStartPageView(TemplateView):
    template_name = "ace_it_test_prep/practice_test_start_page.html"

class PracticeTestView(TemplateView):
    template_name = "ace_it_test_prep/practice_test.html"

    def dispatch(self, request, *args, **kwargs):
        test_session = TestSession.objects.get(user=self.request.user, test_id=kwargs['test_id'])
        print("get_section_statuses: ", get_section_statuses(test_session))
        if get_section_statuses(test_session)[kwargs['section']]:
            kwargs['test_session'] = test_session
            self.create_user_test_responses(**kwargs)
        test_session.started = True
        test_session.save()
        return super().dispatch(request, *args, **kwargs)

    def get_questions(self, **kwargs):
        print("get_questions")
        print(kwargs['test_id'])
        print(kwargs['section'])
        section = kwargs['section'].replace(" ", "_").lower()
        questions = Question.objects.filter(test__id=kwargs['test_id'], section=section).order_by("number")
        return questions

    def create_user_test_responses(self, **kwargs):
        questions = self.get_questions(**kwargs)
        test_session = kwargs['test_session']
        for question in questions:
            new_testresponse = TestResponse(session=test_session, question=question)
            new_testresponse.save()
        test_session.test_responses_have_been_created =  True 
        test_session.save()
        return

    def get_context_data(self, **kwargs):
        questions = self.get_questions(**kwargs)
        q_and_a = self.set_q_and_a(questions)
        time_limit = self.get_time_limit(**kwargs)
        question_nums_range = self.get_question_nums_range(questions)
        print(kwargs['section'])
        context = super().get_context_data(**kwargs)
        if kwargs['section'] == 'Reading':
            passages = self.get_reading_passages(kwargs['test_id'])
            context['passages'] = passages
            passages_list = list(passages)
            context['passage_index'] = passages_list[0]
            print(context['passages'])
        context['q_and_a'] = q_and_a
        context['time_limit'] = time_limit
        context['question_nums_range'] = question_nums_range
        context["test_session_id"] = TestSession.objects.get(user=self.request.user, test_id=kwargs['test_id']).id
        context['section'] = kwargs['section']
        context['question_nums'] = questions.count()
        print("context[test_session_id]******************: ", context["test_session_id"])
       
        return context

    def set_q_and_a(self, questions):
        q_and_a_list = []
        for question in questions:
            answers = list(Answer.objects.filter(question=question).order_by("value").values())
            q_and_a_list.append(
                {
                    "question": model_to_dict(question),
                    "answers": answers
                }
            )
        return q_and_a_list

    def get_time_limit(self, **kwargs):
        # should these be in the DB?
        section = kwargs['section'].replace(" ", "_").lower()
        if section.startswith("math") or section == "verbal":
            return 30
        elif section == "reading":
            return 40        

    def get_question_nums_range(self, questions):
        return range(questions.count())  

    def get_reading_passages(self, test_id):
        return self.serialize_passages(ReadingPassage.objects.filter(test__id=test_id).order_by('passage_index'))
        # return JsonResponse(list(ReadingPassage.objects.filter(test__id=test_id)), safe=False)
        # return json.dumps(serializers.serialize("json", ReadingPassage.objects.filter(test__id=test_id)))

    def serialize_passages(self, passage_qs):
        passages_dict = {}
        passages_list = []
        for passage in passage_qs:
            passages_list.append({
                passage.id :model_to_dict(passage)
            })
            passages_dict[passage.id] = model_to_dict(passage)
        # return json.dumps(passages_list)
        return passages_dict

class SubmitTestView(View):
    def post(self, request, *args, **kwargs):
        test_session_id = request.POST.get("test_session_id")
        section = request.POST.get("section").replace(" ", "_").lower()
        test_session = TestSession.objects.get(id=test_session_id)
        setattr(test_session, f"section_status_{section}", "C")
        if all(status is "C" for status in get_section_statuses(test_session).values()):
            test_session.finished = True
        test_session.save()
        score_test(test_session_id, section)
        if test_session.finished:
            print("session completed")
            return redirect('ace_it_test_prep:practice_test_results_overview', test_session_id=test_session_id)
        else:
            return redirect('ace_it_test_prep:practice_test_detail_view', pk=test_session.test.id)

# This view doesn't seem to be needed?
class PracticeTestResultsOverviewView(ListView):
    print("PracticeTestResultsListView")
    model = TestResponse # should this be TestSession and use that as the view object?
    template_name = "ace_it_test_prep/practice_test_results_overview.html"

    def get_context_data(self, **kwargs):
        test_session_id = self.kwargs['test_session_id']
        test_session = TestSession.objects.get(id=test_session_id)
        context = super().get_context_data(**kwargs)
        context['section_data'] = get_section_statuses(test_session)
        context['test_session_id'] = test_session_id
        print("CONTEXT: ", context)
        return context


class PracticeTestResultsListView(ListView):
    model = TestSession 
    template_name = "ace_it_test_prep/practice_test_results.html"

    def get_context_data(self, **kwargs):
        test_session_id = self.kwargs['test_session_id']
        section = self.kwargs['section'].replace(" ", "_").lower()
        test_session = TestSession.objects.get(id=test_session_id)
        print("section: ", section)
        context = super().get_context_data(**kwargs)
        context['test_session_id'] = test_session_id
        questions = Question.objects.filter(test = test_session.test, section=section).extra({'number_int': "CAST(number as INTEGER)"}).order_by('number_int')
        question_ids = questions.values_list("id", flat=True)
        print("question_ids: ", question_ids)
        user_answers = TestResponse.objects.filter(session=test_session, question__id__in = question_ids).order_by('question__number')
        print("questions: ", questions)
        print("user_answers: ", user_answers)
        context['zipped_data'] = zip(user_answers, questions)
        print("CONTEXT: ", context)
        return context

class PracticeTestResultsDetailView(TemplateView):
    template_name = "ace_it_test_prep/practice_test_results_detail_view.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        test_response = TestResponse.objects.get(id=kwargs['test_response_id'])
        print("test_response: ", test_response, " test_response.id: ", test_response.id)
        question = test_response.question
        # context['next_question_num'], context['previous_question_num'] = self.get_next_and_previous_question_ids(question, test_response)
        context['next_test_response_id'], context['previous_test_response_id'] = self.get_next_and_previous_test_response_ids(test_response)
        q_and_a_dict = self.set_q_and_a(question)
        context['question'] = question
        context['answers'] = list(Answer.objects.filter(question=question).order_by("value").values())
        context['test_session_id'] = test_response.session.id
        context['section'] = question.section
        context['test_response_id'] = test_response.id
        context['test_response'] = test_response
        if question.section == 'reading':
            context['passage'] = ReadingPassage.objects.get(id = test_response.question.passage.id, test=test_response.question.test)
        print("CONTEXT: ", context)
        print(test_response.response)
        return context

    def set_q_and_a(self, question):
        answers = list(Answer.objects.filter(question=question).order_by("value").values())
        q_and_a_dict = {
                "question": model_to_dict(question),
                "answers": answers
            }
        return q_and_a_dict

    def get_next_and_previous_test_response_ids(self, test_response):
        num_questions = Question.objects.filter(test=test_response.session.test, section=test_response.question.section).count()
        if test_response.question.number == 1:
            return TestResponse.objects.filter(session__user=self.request.user, question__section=test_response.question.section, session=test_response.session, question__number__in=[2,num_questions]).values_list('id', flat=True)
        elif test_response.question.number == num_questions:
            return TestResponse.objects.filter(session__user=self.request.user, question__section=test_response.question.section, session=test_response.session, question__number__in=[1,num_questions - 1]).values_list('id', flat=True)
        else:
            return TestResponse.objects.filter(session__user=self.request.user, question__section=test_response.question.section, session=test_response.session, question__number__in=[test_response.question.number + 1,test_response.question.number - 1]).order_by("-question__number").values_list('id', flat=True)

    # def get_next_and_previous_question_ids(self, question, test_response):
    #     num_questions = Question.objects.filter(test=test_response.session.test, section=question.section).count()
    #     if question.number == 1:
    #         return (2, num_questions) 
    #     elif question.number == num_questions:
    #         return (1, num_questions - 1) 
    #     else:
    #         return (question.number + 1, question.number - 1) 

def score_section(response_object, terms):
    results = response_object
    number_correct = 0
    number_incorrect = 0
    number_omitted = 0
    for index, res in enumerate(results):
        print("res['user_selection']: ", res['user_selection'])
        print("res['correct_answer']: ", res['correct_answer'])
        if res['user_selection'] == terms[index]["answer_options"].index(res['correct_answer']):
            res["correct"] = True
            res["omitted"] = False
            number_correct+=1
        elif res['user_selection'] == None:
            res["correct"] = False
            res["omitted"] = True
            number_omitted+=1
        else:
            res["correct"] = False
            res["omitted"] = False
            number_incorrect+=1
    score = dict(
        number_correct = number_correct,
        number_incorrect = number_incorrect,
        number_omitted = number_omitted,
        percent_correct = (number_correct / len(results)) * 100
    )
    
    return (json.dumps(results), score)
    
def score_test(test_session_id, section):
    user_answers = TestResponse.objects.filter(session=test_session_id, question__section=section).order_by('question__id')
    num_correct = 0
    num_incorrect = 0
    num_omitted = 0
    for user_answer in user_answers:
        if int(user_answer.response) == int(user_answer.question.correct_answer):
            print("correct!")
            user_answer.correct = True
            user_answer.answered = True
            num_correct += 1
        elif int(user_answer.response) != -1:
            print("incorrect!")
            user_answer.correct = False
            user_answer.answered = True
            num_incorrect += 1
        else:
            print("omitted!")
            user_answer.correct = False
            user_answer.answered = False
            num_omitted += 1
        user_answer.save()
    return (num_correct, num_incorrect, num_omitted)


# def submit_section_old(request):
#     test_session_id = request.POST.get("test_session_id")
#     section = request.POST.get("section")
#     test_session = TestSession.objects.get(id=test_session_id)
#     test_session_sections = test_session.testsessionsection_set.all()
#     test_session_section = test_session_sections.get(section__name=section)
#     test_session_section.completed = True
#     test_session_section.save()

#     student_id = Student.objects.get(user_profile__user=test_session.user)

#     sections_completed = test_session_sections.values_list("completed", flat=True)

#     print("sections_completed: ", sections_completed)
#     # print("test_session_section.values: ", test_session_section.values())

#     if sections_completed.count() == 4 and False not in sections_completed:
#         print("TRUE")
#         test_session.completed =  True
#         test_session.save()
#         assignmentsession = test_session.assignmentsession_set.first()
#         if assignmentsession:
#             print("assignmentsession: ", assignmentsession.assignment)
#             assignment = assignmentsession.assignment
#             assignment.completed = True
#             assignment.save()

#     print("test_session_section: ", test_session_section.completed)

    # user_answers = TestResponse.objects.filter(session=test_session_id).order_by('question__id')
    # user_answers_serialized = serializers.serialize("json", user_answers, fields=('question', 'response'))
    # score_test(test_session_id)
    # return render(request, "ace_it_test_prep/practice_test_detail.html")
    # will redirect to practice detail page until test is complete when page will redirect
    # to results page

    # print("test_session.completed: ", test_session.completed)

    # if test_session.completed:
    #     print("session completed")
    #     return redirect('ace_it_test_prep:practice_test_results_overview', test_session_id=test_session_id)
    # else:
    #     return redirect('ace_it_test_prep:practice_test_detail', test_id=test_session.test.id, student_id=student_id)

    # return redirect('ace_it_test_prep:practice_test_detail', test_id=test_session.test.id) 

# def account_home(request, profile_type=None):
#     user = User.objects.get(id=request.user.id)
#     print("user: ", user)
#     print("user type: ", type(user))
#     user_profile = UserProfile.objects.get(user=user)
#     user_type = user_profile.user_type.capitalize()
#     user_profile_model = apps.get_model("ace_it_test_prep", user_type)
#     user_type_profile = user_profile_model.objects.get(user_profile=user_profile)
#     print("user_type_profile: ", user_type_profile)

#     if user_type == "Student":
#         context = prepare_student_account_page(user, user_profile, user_type, user_type_profile)
        
#         print("context: ", context)
#         return render(request, "ace_it_test_prep/account_home.html", context)

#     elif user_type == "Parent":
#         pass
#     elif user_type == "Instructor":
#         students = Student.objects.filter(instructor=user_type_profile)
#         context = {
#             "profile_type": user_profile.user_type,
#             "students": students
#         }
#         return render(request, "ace_it_test_prep/instructor_home.html", context)
    

# def serialize_ssat_practice_tests(user):
#     ssat_practice_test_list = []
#     ssat_practice_tests = Test.objects.filter(test_type="ssat")
#     print("ssat_practice_tests: ", ssat_practice_tests)
    
#     user_test_sessions = TestSession.objects.filter(user=user, test__test_type="ssat")
#     print("user_test_sessions: ", user_test_sessions)
#     fields = TestSession._meta.fields 
#     for f in fields:
#         print(f)
#     if user_test_sessions.exists():
#         print(user_test_sessions is not None)
#         completed_ssat_practice_tests_qs = user_test_sessions.filter(time_finished is not None)
#         completed_ssat_practice_tests_ids = list(completed_ssat_practice_tests_qs.values_list("test_id", flat=True))

#         started_ssat_practice_tests_qs = user_test_sessions.filter(started=True)
#         started_ssat_practice_tests_ids = list(started_ssat_practice_tests_qs.values_list("test_id", flat=True))

#         print("completed_ssat_practice_tests_ids: ", completed_ssat_practice_tests_ids)
#     else:
#         completed_ssat_practice_tests_ids = []
#         started_ssat_practice_tests_ids = []

    # test_sessions_completed = list(TestSession.objects.filter(user=user, test__id__in=completed_ssat_practice_tests_ids).values_list("test_id", flat=True))
    # test_sessions_started = completed_ssat_practice_tests_qs.values_list("test_id", flat=True))
    # print("test_sessions_completed: ", test_sessions_completed)


    # for ssat_practice_test in ssat_practice_tests:
    #     if ssat_practice_test.question_set.all().count() > 0 and ssat_practice_test.test_type == "ssat":
    #         if ssat_practice_test.id in completed_ssat_practice_tests_ids:
    #             print("IN")
    #             test_status = "completed"
    #             test_session = completed_ssat_practice_tests_qs.get(test__id=ssat_practice_test.id)
    #         else:
    #             if ssat_practice_test.id in started_ssat_practice_tests_ids:
    #                 print("IN")
    #                 test_status = "started"
    #                 test_session = started_ssat_practice_tests_qs.filter(test__id=ssat_practice_test.id)
    #             else:
    #                 print("OUT")
    #                 test_status = "not started"
    #                 test_session = None

    #         ssat_practice_test_list.append({
    #             "practice_test": ssat_practice_test,
    #             "test_status": test_status,
    #             "test_session": test_session
    #             })

    # print("ssat_practice_tests: ", ssat_practice_tests)
    # print("ssat_practice_test_list***: ", ssat_practice_test_list)

    # return ssat_practice_test_list

# def get_next_exercise(user):
#     fields = PracticeSession._meta.fields 
#     for f in fields:
#         print(f)
#     completed_practice_sessions_ids = PracticeSession.objects.exclude(score = None).values_list('id', flat=True)
#     try:
#         next_practice_exercise = PracticeExercise.objects.exclude(id__in=completed_practice_sessions_ids).first()
#     except Exception as e:
#         print("Exception: ", e)
#     return next_practice_exercise

# def prepare_student_account_page(user, user_profile, user_type, user_type_profile):
#     ssat_practice_test_list = serialize_ssat_practice_tests(user)
#     recommended_next_exercise = get_next_exercise(user)

#     print("recommended_next_exercise: ", recommended_next_exercise)

#     instructor = user_type_profile.instructor
#     print("Instructor: ", instructor)
#     test_type = user_type_profile.prep_for_test_type
#     print("test_type??????: ", test_type)

#     student_id = user_type_profile.id

#     assignments = Assignment.objects.filter(instructor=instructor, student=user_type_profile)

#     incomplete_assignments = assignments.filter(completed=False)
#     completed_assignments = assignments.filter(completed=True)

#     context = {
#         "ssat_practice_test_list": ssat_practice_test_list,
#         "profile_type": user_profile.user_type,
#         "instructor": instructor,
#         "test_type": test_type,
#         "incomplete_assignments": incomplete_assignments,
#         "completed_assignments": completed_assignments,
#         "student_id": student_id,
#         "recommended_next_exercise": recommended_next_exercise
#     }
#     return context



# def student_profile(request, student_id):
#     student = Student.objects.get(id=student_id)
#     # print("student: ", student.values())
#     instructor = Instructor.objects.get(user_profile__user=request.user)
#     tests = Test.objects.filter(test_type=student.prep_for_test_type.lower())
#     assigned_tests = []
#     completed_tests = []
#     for test in tests:
#         assignments = test.assignment_set.filter(student=student, instructor=instructor)
#         for assignment in assignments:
#             if assignment.completed:
#                 completed_tests.append(assignment)
#             else:
#                 assigned_tests.append(assignment)
#     print("assigned_tests: ", assigned_tests)
#     print("completed_tests: ", completed_tests)
#     context = {
#         "student": student,
#         "tests": tests,
#         "assigned_tests": assigned_tests,
#         "completed_tests": completed_tests
#     }

#     ##Should there be a model for assignments from instructor to student?##
#     return render(request, "ace_it_test_prep/student_profile.html", context)

# def assign_to_student(request, test_id, student_id):
#     print("test_id: ", test_id)
#     print("student_id: ", student_id)
#     student = Student.objects.get(id=student_id)
#     test = Test.objects.get(id=test_id)
#     context = {
#         "student": student,
#         "test": test
#     }
#     return render(request, "ace_it_test_prep/assign_to_student.html", context)

# def save_new_assignment(request):
#     student_id = request.POST.get("student_id")
#     test_id = request.POST.get("test_id")
#     due_date = request.POST.get("due_date")
#     instructor = Instructor.objects.get(user_profile__user=request.user)
#     student = Student.objects.get(id=student_id)
#     test = Test.objects.get(id=test_id)
#     new_assignment = Assignment(instructor=instructor, student=student, test=test, due_date=due_date)
#     new_assignment.save()
#     return redirect("ace_it_test_prep:student_profile", student_id=student_id)

# def add_student(request):
#     return render(request, "ace_it_test_prep/add_student.html")

# def invite_student(request):
#     student_email = request.POST.get('student_email')
#     student_user = User.objects.get(email=student_email)
#     student = Student.objects.get(user_profile__user=student_user)
#     instructor = Instructor.objects.get(user_profile__user = request.user)
#     student.instructor = instructor
#     student.save()
#     print("instructor: ", instructor)
#     instructor_student_list = Student.objects.filter(instructor=instructor)
#     print("student: ", student)
#     print("instructor_student_list: ", instructor_student_list)
#     return HttpResponse("Success")


# def reading_practice_overview(request):
#     return render(request, "ace_it_test_prep/reading_practice_overview.html")

# def verbal_practice_overview(request):
#     return render(request, "ace_it_test_prep/verbal_practice_overview.html")

# def vocabulary_practice(request):
#     vocabulary_terms = VocabularyTerm.objects.all()
#     num_terms = vocabulary_terms.count()
#     id_list = []
#     for i in range(0,5):
#         id_list.append(random.randint(1,num_terms))
#     practice_terms = vocabulary_terms.filter(id__in=id_list)
#     practice_terms_serialized = serializers.serialize("json", practice_terms)

#     context = {
#         "first_term": practice_terms[0],
#         "serialized_data": practice_terms_serialized
#     }
#     print("practice_terms: ", practice_terms)
#     return render(request, "ace_it_test_prep/vocabulary_practice.html", context)

# def vocabulary_roots_practice(request, root=None):
    # if root:
    #     practice_terms = VocabularyTerm.objects.filter(vocabulary_root=root) 
    #     practice_terms_serialized = serializers.serialize("json", practice_terms)
    #     first_term = practice_terms[0]
    #     print("first_term: ", first_term)
    #     context = {
    #         "first_term": first_term,
    #         "terms_json": practice_terms_serialized
    #     }
    #     print("context: ", context)
    #     return render(request, "ace_it_test_prep/vocabulary_flashcards.html", context)
    # else:
    #     roots = VocabularyRoot.objects.all()
    #     context = {
    #         "roots": roots
    #     }
    #     return render(request, "ace_it_test_prep/vocabulary_roots_options_overview.html", context)

#     practice_terms = VocabularyRoot.objects.all()
#     practice_terms_serialized = serializers.serialize("json", practice_terms)
#     first_term = practice_terms[0]
#     print("first_term: ", first_term)
#     context = {
#         "first_term": first_term,
#         "terms_json": practice_terms_serialized
#     }
#     print("context: ", context)
#     return render(request, "ace_it_test_prep/vocabulary_flashcards.html", context)

# def vocabulary_derivatives_practice(request, root=None):
#     print("DERIVATIVES PRACTICE")
#     if root:
#         print("IF")
#         practice_terms = VocabularyTerm.objects.filter(vocabulary_root_id=root) 
#         practice_terms_serialized = serializers.serialize("json", practice_terms)
#         first_term = practice_terms[0]
#         print("first_term: ", first_term)
#         context = {
#             "first_term": first_term,
#             "terms_json": practice_terms_serialized
#         }
#         print("context: ", context)
#         return render(request, "ace_it_test_prep/vocabulary_flashcards.html", context)
#     else:
#         print("ELSE")
#         roots = VocabularyRoot.objects.exclude(vocabularyterm=None)
#         context = {
#             "roots": roots
#         }
#         return render(request, "ace_it_test_prep/vocabulary_roots_options_overview.html", context)
    

# def vocabulary_roots_practice_synonyms(request):
    # num_entities = VocabularyTermSynonym.objects.all().count()
    # rand_entities = random.sample(range(num_entities), 10)
    # sample_entities = VocabularyTermSynonym.objects.filter(id__in=rand_entities)
#     synonyms = VocabularyTermSynonym.objects.all()
#     synonyms_list = []
#     number = 1

#     for synonym in synonyms:

#         new_synonym = {
#             "question": synonym.term.term,
#             "question_id": synonym.id,
#             "number": number,
#             "answer_options": [
#                 synonym.option_a,
#                 synonym.option_b,
#                 synonym.option_c,
#                 synonym.option_d,
#                 synonym.option_e,
#             ],
#             "correct_answer": synonym.correct_answer
#         }
#         synonyms_list.append(new_synonym)
#         number += 1

#     context = { "terms": new_synonym, "terms_json": json.dumps(synonyms_list) }
#     print("context: ", context)
#     return render(request, "ace_it_test_prep/mcq.html", context)

# def vocabulary_by_category(request, category=None):
#     if category:
#         practice_terms = VocabularyTerm.objects.filter(vocabulary_central_idea__idea_name=category)
#         practice_terms_serialized = serializers.serialize("json", practice_terms)
#         first_term = practice_terms[0]
#         print("first_term: ", first_term)
#         context = {
#             "first_term": first_term,
#             "terms_json": practice_terms_serialized
#         }
#         print("context: ", context)
#         return render(request, "ace_it_test_prep/vocabulary_flashcards.html", context)
#     else:
#         categories = VocabularyCentralIdea.objects.all()
#         context = {
#             "categories": categories
#         }
#         return render(request, "ace_it_test_prep/vocabulary_options_overview.html", context)

# def vocabulary_flashcards_overview(request):
#     return render(request, "ace_it_test_prep/vocabulary_flashcards_overview.html")

# def mcq_section(request):
#     practice_set_id = request.POST.get("practice_set_id")


# def mcq_submit_section(request):
#     response_object = json.loads(request.POST.get('response_object'))
#     json_terms = request.POST.get('terms')
#     terms = json.loads(json_terms)
#     print("terms: ", terms)
#     score_section_response = score_section(response_object, terms)
#     results = score_section_response[0]
#     scores = score_section_response[1]
#     context = { 'results': results, 'terms': terms, "json_terms": json_terms, "scores": scores }
#     print("context: ", context)
#     # print("scores: ", scores)
#     return render(request, "ace_it_test_prep/mcq_results_overview.html", context)



# def mcq_results_detail(request):
#     results = request.POST.get("results") 
#     terms = request.POST.get("terms") 
#     scores = request.POST.get("scores") 
#     print("results: ", results)
#     print("terms: ", terms)
#     print("scores: ", scores)
#     context = {
#         "terms": json.loads(terms)
#     }
#     print("CONTEXT: ", context["terms"][0])
#     return render(request, "ace_it_test_prep/mcq_results_detail.html", context)

# def test_synonyms(request):
#     print("data: ", request.POST.get("serialized_data"))
#     test_synonyms_data = json.loads(request.POST.get("serialized_data"))
#     all_vocabulary_terms = VocabularyTerm.objects.all()
#     all_vocabulary_terms_count = all_vocabulary_terms.count()
#     all_terms = []
#     all_terms_serialized = []
#     term_data = []
#     for tested_term in test_synonyms_data:
#         print(tested_term)
#         print("\n")
#         tested_term_id = tested_term["pk"]
#         distractor_ids = []
#         for i in range(0,4):
#             distractor_id = random.randint(0, all_vocabulary_terms_count)
#             while distractor_id == tested_term_id:
#                 distractor_id = random.randint(0, all_vocabulary_terms_count)
#             distractor_ids.append(distractor_id)

#         answer_options_list = list(all_vocabulary_terms.filter(id__in=distractor_ids).values_list("term", flat=True))

#         correct_answer_index = random.randint(0,4)
#         for index in range(0,5):
#             if index == correct_answer_index:
#                 synonym_index = random.randint(0,2)
#                 possible_correct_answers = all_vocabulary_terms.filter(id=tested_term_id).values_list("synonyms_list", flat=True)[0].split(", ")
#                 answer_options_list.insert(index, possible_correct_answers[synonym_index].strip(" ").capitalize())

#         print("answer_options_list$$$: ", answer_options_list)
#         print("answer_options_list: ", type(answer_options_list))

#         tested_term_and_distractor_ids = []
#         tested_term_and_distractor_ids.append(tested_term_id)
#         tested_term_and_distractor_ids.extend(distractor_ids)
#         random.shuffle(tested_term_and_distractor_ids)
#         print("tested_term_and_distractor_ids: ", tested_term_and_distractor_ids)

#         distractor_qs = all_vocabulary_terms.filter(id__in=distractor_ids)
#         distractor_serialized = serializers.serialize("json", distractor_qs)

#         distractor_list = []
#         for distractor in distractor_qs:
#             print(distractor)
#             distractor_list.append({
#                 "term": distractor.term,
#                 "correct": False
#             })

#         # tested_term_synonyms_list = tested_term["fields"]["synonyms_list"].join(",")
#         # random.shuffle(tested_term_synonyms_list)
#         #
#         # distractor_list.extend({
#         #     "term": tested_term_synonyms_list[0],
#         #     "correct": True
#         # })

#         term_data = {
#             "tested_term": tested_term["fields"]["term"],
#             "answer_options_list": answer_options_list,
#             "correct_answer_index": correct_answer_index
#         }

#         term_data_serialized = {
#             "tested_term": tested_term["fields"],
#             "distractors": distractor_serialized
#         }

#         all_terms_serialized.append(term_data_serialized)
#         all_terms.append(term_data)
#     print("all_terms: ", all_terms[0])
#     print("all_terms type: ", type(all_terms[0]))
#     context = {
#         # "tested_term": tested_term["fields"]["term"],
#         # "first_term_data": json.loads(term_data[0]),
#         # "term_data_json": json.dumps(term_data)
#         "term_data": all_terms,
#         "term_data_json": json.dumps(all_terms),
#         # "term_data_json": json.dumps(all_terms_serialized)
#     }
#     return render(request, "ace_it_test_prep/practice_synonyms.html", context)

# def score_synonyms_practice(request):
#     user_answer_selections = request.POST.get("user_answer_selections").split(",")
#     term_data = request.POST.get("term_data")
#     jsonified = term_data.replace("\'", "\"")
#     term_data = json.loads(request.POST.get("term_data").replace("\'", "\""))
#     term_data_results = term_data

#     index = 0
#     score = 0
#     for term in term_data:
#         print("term: ", term)
#         if term["correct_answer_index"] == user_answer_selections[index]:
#             score += 1
#         term_data_results[index]["user_answer_selection"] = user_answer_selections[index]

#     context = {
#         "term_data_results": term_data_results,
#         "score": score
#     }

#     print("contex: ", context)
#     return render(request, "ace_it_test_prep/synonyms_practice_results.html", context)

# def math_practice_overview(request):
#     return render(request, "ace_it_test_prep/math_practice_overview.html")

# def get_sections_data(sections, test_session):
#     sections_data = []
#     # if test_session.count() > 0:
#     #     test_session = test_session[0]
#     user_test_session_sections = TestSessionSection.objects.filter(test_session=test_session, completed=True).values_list("section__name", flat=True)
#     test_session_id = test_session.id
#     print("user_test_session_sections: ", user_test_session_sections)
#     for section in sections:
#         print("section: ", section)
#         if section in user_test_session_sections:
#             sections_data.append({"section":section, "completed":True})
#         else:
#             sections_data.append({"section":section, "completed":False})
    # else:
        # test_session_id = ""
        # for section in sections:
        #     sections_data.append({"section":section, "completed":False})

    # return sections_data, test_session_id


# def practice_test_detail(request, test_id, student_id):
#     print("PRACTICE TEST DETAIL")

#     test = Test.objects.filter(id=test_id)[0]

#     user_profile = UserProfile.objects.get(user=request.user)

#     print("user_profile.user_type: ", user_profile.user_type)
#     if user_profile.user_type == "student":
#         print("Student")
#         test_session, created = TestSession.objects.get_or_create(user=request.user, test=test)
#         print("created: ", created)
#         print("test_session: ", test_session)
#         # if not created:
#         #     test_session = test_session[0]
#     elif user_profile.user_type == "instructor":
#         print("Instructor")
#         student_user = Student.objects.get(id=student_id)
#         test_session = TestSession.objects.get(user=student_user.user_profile.user, test__id=test_id)


#     if created:
#         # test_session.started = True
#         all_questions = Question.objects.filter(test=test_session.test)
#         create_answer_responses(test_session, all_questions)

#     sections = Section.objects.filter(test_type=test.test_type).values_list("name", flat=True).order_by("rank")
#     sections_data = []

#     sections_data, test_session_id = get_sections_data(sections, test_session)

    # if test_session.count() > 0:
    #     test_session = test_session[0]
    #     user_test_session_sections = TestSessionSection.objects.filter(test_session=test_session, completed=True).values_list("section__name", flat=True)
    #     test_session_id = test_session.id
    #     print("test_session: ", test_session.id)
    #     print("user_test_session_sections: ", user_test_session_sections)
    #     for section in sections:
    #         print("section: ", section)
    #         if section in user_test_session_sections:
    #             sections_data.append({"section":section, "completed":True})
    #         else:
    #             sections_data.append({"section":section, "completed":False})
    # else:
    #     test_session_id = ""
    #     for section in sections:
    #         sections_data.append({"section":section, "completed":False})

    # print("test_session: ", test_session)

    # context = {
    #     "test_id": test_id,
    #     "test_session_id": test_session_id,
    #     "sections_data": sections_data,
    #     "user": test_session.user
    # }
    # print("context: ", context)
    # return render(request, "ace_it_test_prep/practice_test_detail.html", context)

# def practice_test_start_page(request, id, section):
#     print("id: ", id)
#     print("section: ", section)
#     context = {
#         "test_id": id,
#         "section": section
#     }
#     return render(request, "ace_it_test_prep/practice_test_start_page.html", context)

# def practice_test(request, test_id, section):
#     print("PRACTICE TEST")
#     print("test_id: ", test_id)
#     print("section: ", section)
#     test = Test.objects.get(id=test_id)
#     section=Section.objects.get(name=section)
#     print("section: ", section)
#     test_session, session_created = TestSession.objects.get_or_create(user=request.user, test=test)
#     test_session_section, session_section_created = TestSessionSection.objects.get_or_create(
#         test_session=test_session,
#         section=section,
#         # start_date=,
#         # end_date=,
#         started=True
#     )

#     all_questions = Question.objects.filter(test=test_session.test).order_by("number")
#     section_questions = all_questions.filter(section=section)
#     section_questions_num = section_questions.count()
#     # print("section_questions: ", section_questions)
#     # print("questions.values_list('id', flat=True): ", list(section_questions.values_list('id', flat=True)))
    
    
#     if section.name == "reading":
#         print("READING")
#         passage_ids = list(section_questions.values_list('passage__id', flat=True))
#         # print("passage_ids: ", passage_ids, " passage_ids_type: ", type(passage_ids))
#         passages = ReadingPassage.objects.filter(id__in=passage_ids)
#         # print("passages: ", passages)
#         serialized_passages = json.dumps(serializers.serialize("json", passages))
#         # print("serialized_passages: ", serialized_passages)
#         # print("serialized_passages: ", json.dumps(serialized_passages))
#     else:
#         print("NOT Reading")
#         serialized_passages = "null"      

#     #moved to practice_test_detail
#     # if session_created:
#     #     # test_session.started = True
#     #     create_answer_responses(test_session, all_questions)

#     data = get_answers(section_questions)
#     # print("data[0]: ", data[0])

#     assignments = Assignment.objects.filter(student__user_profile__user=request.user)

#     if assignments.filter(test=test).exists():
#         assignment = assignments.filter(test=test).first()
#         new_assignmentsession, assignmentsession_created = AssignmentSession.objects.get_or_create(assignment=assignments.filter(test=test).first(), test_session=test_session)
#         if assignmentsession_created:
#             new_assignmentsession.save()
#             assignment.started = True
#             assignment.save()


#     # print("data: ", data)
#     context = {
#         "test_session_id": test_session.id,
#         "data": data,
#         "question_nums_range": range(section_questions_num),
#         "question_nums": section_questions_num,
#         "section": section,
#         # "passages": passages,
#         "passages": serialized_passages,
#         # "passages": "passages",
#         "time_limit": section.time_limit,
#         "testing": "testing***"
#     }

#     # print("pratice_test context: ", context)

#     return render(request, "ace_it_test_prep/practice_test.html", context)

# def get_answers(questions):
#     questions_values = questions.values()
#     # print("questions_values: ", questions_values[0])
#     # for question in questions_values:
#         # print("question: ", question)
#         # answers = question.answer_set.all()
#         # print("answers: ", answer)
#     data = []
#     if isinstance(questions, QuerySet):
#         for question in questions:
#             answers_list = format_answers(question.answer_set.all())
#             # print("answers_list: ", answers_list)
#             if question.question_type is None:
#                 question.question_type = "None"
#             # if question.passage is None:
#             #     print("NO PASSAGE")
#             #     question.passage = "None"
#             if question.diagram_src is None:
#                 question.diagram_src = "None"
#             data.append({ "question": model_to_dict(question), "answers": answers_list })
#     else:
#         answers_list = format_answers(questions.answer_set.all())
#         data.append({ "question": model_to_dict(questions), "answers": answers_list })
#     return data

# def format_answers(answers):
#     answers_list = []
#     for answer in answers:
#         # print("ANSWER: ", answer.num_students_choice)
#         if answer.num_students_choice is None:
#             answer.num_students_choice = 0
#         # print("ANSWER: ", answer.num_students_choice)
#         answers_list.append(model_to_dict(answer))
#     # print("answers_list: ", answers_list)
#     return answers_list

# def create_test_session(user, test):
#     print("create_test_session")
#     test_session = TestSession()
#     test_session.user = user
#     test_session.test = test
#     test_session.save()
#     return test_session

# def create_answer_responses(test_session, questions):
#     count = 0
#     for question in questions:
#         test_response = TestResponse(session=test_session, question=question)
#         test_response.save()
#         count += 1

#     print("COUNT: ", count)



# def get_question(request):
#     body_unicode = request.body.decode('utf-8')
#     body = json.loads(body_unicode)
#     print("body['test_session_id']: ", body['test_session_id'])
#     print("body['questionNum']: ", body['questionNum'])
#     test_session = TestSession.objects.get(id=body['test_session_id'])

#     qs = Question.objects.filter(test=test_session.test)
#     nums = qs.count()
#     create_answer_responses(test_session, qs)

#     data_list = []

#     for question in qs:
#         answers = question.answer_set.all()
#         data_list.append({
#             "question": json.loads(question),
#             "answers": json.loads(answers)
#         })

#     print("DATA_LIST: ", data_list)

#     first_question = Question.objects.get(test=test_session.test, number=body['questionNum'])
#     # first_question_answers = Answer.objects.all()
#     first_question_answers = first_question.answer_set.all()
#     # first_question_serialized = serializers.serialize("json", first_question)
#     first_question_answers_serialized = serializers.serialize("json", first_question_answers)
#     print("first_question: ", first_question)
#     print("first_question_answers: ", first_question_answers)
#     data = {
#         "nums": nums,
#         "first_question": model_to_dict(first_question),
#         "first_question_answers": first_question_answers_serialized
#     }
#     print("DATA: ", data)
#     return JsonResponse(data, content_type='application/json')

# def get_questions(request):
#     print("************GETQUESTIONS")
#     print("request: ", request)
#     body_unicode = request.body.decode('utf-8')
#     body = json.loads(body_unicode)
#     print("body['test_session_id']: ", body['test_session_id'])
#     test_session_id = body['test_session_id']
#     section = body['section']
#     print("section: ", section)
#     test_session = TestSession.objects.get(id=test_session_id)
#     # test_session = TestSession.objects.get(user=request.user, test=test)
#     passages = ReadingPassage.objects.filter(test=test_session.test)

#     questions = Question.objects.filter(test=test_session.test, section=section).extra({'number_int': "CAST(number as INTEGER)"}).order_by('number_int')
#     data = get_answers(questions)

#     nums = questions.count()

#     context = {
#         "test_session_id": test_session.id,
#         "data": data,
#         "nums": nums,
#         "passages": serializers.serialize("json", passages)
#     }

    # grouped_answers = group_answers(qs, ans)
    # print("grouped_answers: ", grouped_answers)
    # create_answer_responses(test_session, qs)
    # nums = qs.count()
    # print(qs)
    # # data = json.dumps(questions)
    # # context = {"data": data}
    # questions = serializers.serialize("json", qs, fields=('question'))
    # answers = serializers.serialize("json", ans)
    # print("answers: ", answers)
    # context = {
    #     "nums": nums,
    #     "questions": questions,
    #     "answers": answers,
    #     "test_session_id": test_session.id
    # }
    # print("context: ", context)

    # return JsonResponse(context, content_type='application/json')

# def group_answers(qs, ans):
#     ans_list = []
#     q_id = qs[0].id
#     index = 0
#     for question in qs:
#         print("GSDAGAGA: ", type(ans.filter(question__id=question.id)))
#         ans_list.append(ans.filter(question__id=question.id))
#         index += 1
#     return ans_list





# def practice_test_results_overview(request, test_session_id):
#     print("practice_test_results_overview")
#     test_session = TestSession.objects.get(id=test_session_id)
#     print("test_session!!!!: ", test_session)
#     test = test_session.test
#     sections = Section.objects.filter(test_type=test.test_type).values_list("name", flat=True).order_by("rank")
#     print("section")
#     sections_data = []

#     sections_data, test_session_id = get_sections_data(sections, test_session)

#     student_user_profile = UserProfile.objects.get(user=test_session.user)
#     student_id = Student.objects.get(user_profile=student_user_profile)

#     context = {
#         "test_id": test.id,
#         "test_session_id": test_session.id,
#         "sections_data": sections_data,
#         "user": test_session.user,
#         "student_id": student_id
#     }
    # print("context: ", context)
    # return render(request, "ace_it_test_prep/practice_test_results_overview.html", context)

    # if test_session.finished:
    #     print("session completed")
    #     return render(request, 'ace_it_test_prep/practice_test_results_overview.html', context)
    # else:
    #     return render(request, 'ace_it_test_prep/practice_test_detail.html', context)



# def practice_test_results(request, test_session_id, section=None):
#     print("SECTION: ", section)
#     print("test_session_id$$$$$ ", test_session_id)
#     print("test_session_id$$$$$ ", type(test_session_id))
#     test_session = TestSession.objects.get(id = test_session_id)
#     questions = Question.objects.filter(test = test_session.test, section=section).extra({'number_int': "CAST(number as INTEGER)"}).order_by('number_int')
#     question_ids = questions.values_list("id", flat=True)
#     print(question_ids)
#     # user_answers = questions.testresponse_set.all()
#     user_answers = TestResponse.objects.filter(session=test_session, question__id__in = question_ids).order_by('question__number')
#     # for question in questions:
#     #     user_answers.append(TestResponse.objects.filter(question = question))
#     # user_answers = TestResponse.objects.filter(session__id = test_session_id)
#     test_id = test_session.test.id
#     # print("user_answers!!!: ", user_answers.count())
#     print("user_answers!!!: ", user_answers)
#     print("all_questions!!!: ", questions)
#     # print("questions@@@: ", user_answers[0].correct)
#     # print("questions&&&: ", user_answers[1].correct)
#     print(questions[0].__dict__)
#     print("question 1: ",questions[0])
#     zipped_data = zip(user_answers, questions)
#     # context = {
#     #     'user_answers': user_answers,
#     #     'questions': questions
#     # }

#     num_correct = user_answers.filter(correct = True).count()
#     num_incorrect = user_answers.filter(answered = True, correct = False).count()
#     num_omitted = user_answers.filter(answered = False).count()

#     user_profile = UserProfile.objects.get(user=request.user)

#     print("user_profile: ", user_profile.user_type)

#     if user_profile.user_type == "student":
#         student = Student.objects.get(user_profile=user_profile)
#     elif user_profile.user_type == "instructor":
#         student = Student.objects.get(user_profile__user=test_session.user)

#     print("student: ", student.user_profile.user.first_name)

#     data = {
#         'zipped_data': zipped_data,
#         "test_session_id": test_session.id,
#         "test_id": test_id,
#         "student": student,
#         "num_correct": num_correct,
#         "num_incorrect": num_incorrect,
#         "num_omitted": num_omitted
#     }
    # for ans, q in zipped_data:
    #     print("question_id: ", q.id, "question_text: ", q.question_text)
    #     print("answer_question_id: ", ans.question.id, "answer.response: ", ans.response)

    # print("zipped_data09090909: ", zipped_data[0])
    # print("zipped_data09090909: ", zipped_data.questions)
    # return render(request, "ace_it_test_prep/practice_test_results.html", data)

# def practice_test_results_detail_view(request):
#     print("DETAILS")
#     # test_id = request.POST.get("test_id")
#     # print("test_id: ", test_id)
#     # print("test_id TYPE: ", type(test_id))
#     test_response_id = request.POST.get("test_response_id")
#     section = request.POST.get("section")
#     print("test_response_id: ", test_response_id)
#     test_response = TestResponse.objects.get(id=test_response_id)
#     test_session_id = test_response.session.id
#     action = request.POST.get('action')
#     # question_id = request.POST.get("question_id")
#     question_id = test_response.question.id
#     print("question_id: ", question_id)
#     current_question = Question.objects.get(id=question_id)
#     # question_number = int(current_question.number)
#     # print("question_numberA: ", question_number)
#     questions = Question.objects.filter(test = current_question.test, section=current_question.section)
#     num_of_questions = questions.count()
#     # # print("questions: ", num_of_questions)
#     if action == "next":
#         print("NEXT")
#         next_number = int(current_question.number) + 1
#         # # print("next_number: ", next_number)

#         if next_number > num_of_questions:
#             next_number = 1

#         next_question = questions.get(number = next_number)
#         current_question = next_question
#         test_response = TestResponse.objects.get(session__user=request.user, question=current_question)
#     elif action == "back":
#         print("BACK")
#         next_number = int(current_question.number) - 1
#         if next_number == 0:
#             next_number = num_of_questions
#         next_question = questions.get(number = next_number)
#         current_question = next_question
#         test_response = TestResponse.objects.get(session__user=request.user, question=current_question)
    # print("question_numberB: ", question_number)
    # question = questions.get(number = question_number, test = test_response.session.test)
    # print("PPPPP: ", test_session_id)
    # print("PPPPP: ", question)
    # test_response = TestResponse.objects.filter(session_id=test_session_id, question=question).first()
    # print("test_response: ", test_response)
    # test_response_id = test_response.id
    # answers = current_question.answer_set.all()
    # answers_list = []
    # print("answers: ", answers)
    # for answer in answers:
    #     answers_list.append(model_to_dict(answer))

    # print("answers_list******: ", answers_list)



    # context = {
    #     "test_response": test_response,
    #     "question": current_question,
    #     "answers": answers,
    #     "test_session_id": test_session_id
    # }

    # print("CONTEXT: ", context)
    # return render(request, "ace_it_test_prep/practice_test_results_detail_view.html", context)
