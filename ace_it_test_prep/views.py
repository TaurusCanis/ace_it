from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Question, Test, TestSession, TestResponse, Answer, VocabularyTerm, ReadingPassage, Section, TestSessionSection, Student, Parent, Instructor, UserProfile, Assignment, AssignmentSession
from django.core import serializers
from django.forms.models import model_to_dict
from django.db.models.query import QuerySet
import json, random
from django.contrib.staticfiles.storage import staticfiles_storage
from django.apps import apps

# Create your views here.

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

def index(request):
    return render(request, "ace_it_test_prep/index.html")

def signup(request):
    first_name = request.POST.get("first_name")
    last_name = request.POST.get("last_name")
    username = request.POST.get("username")
    password = request.POST.get("password")
    test_selection = request.POST.get("test_selection")
    prep_for_test_type = request.POST.get("test_selection")
    user_type = request.POST.get("user_type")

    print("username: ", username)
    print("password: ", password)
    print("test_selection: ", test_selection)
    print("user_type: ", user_type)
    print("prep_for_test_type: ", prep_for_test_type)

    user = User.objects.create_user(username, username, password, first_name=first_name, last_name=last_name)
    user_profile = UserProfile.objects.create(user=user, user_type=user_type)

    if user_type == "student":
        print("student")
        new_student_profile = Student.objects.create(user_profile=user_profile, prep_for_test_type=prep_for_test_type)
        # new_student_profile.prep_for_test_type = prep_for_test_type
    elif user_type == "parent":
        print("parent")
        new_parent_profile = Parent.objects.create(user_profile=user_profile)
    else:
        print("instructor")
        new_instructor_profile = Instructor.objects.create(user_profile=user_profile)

    login(request, user)

    profile_type = user_profile.user_type

    return redirect('ace_it_test_prep:account_home', profile_type=profile_type)
    # return render(request, "ace_it_test_prep/account_home.html", context)

def login_user(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    user = authenticate(request, username=username, password=password)
    print("user: ", user)
    user_profile = UserProfile.objects.get(user=user)
    profile_type = user_profile.user_type
    if user is not None:
        login(request, user)
        context = {
            "profile_type": profile_type
        }
        return redirect('ace_it_test_prep:account_home', profile_type=profile_type)
    else:
        return render(request, "ace_it_test_prep/index.html")

def logout_user(request):
    logout(request)
    return render(request, "ace_it_test_prep/index.html")

def account_home(request, profile_type=None):
    user = User.objects.get(id=request.user.id)
    print("user: ", user)
    print("user type: ", type(user))
    user_profile = UserProfile.objects.get(user=user)
    user_type = user_profile.user_type.capitalize()
    user_profile_model = apps.get_model("ace_it_test_prep", user_type)
    user_type_profile = user_profile_model.objects.get(user_profile=user_profile)
    print("user_type_profile: ", user_type_profile)

    if user_type == "Student":

        # if profile_type:
        print("profile_type: ", profile_type)
        ssat_practice_tests = Test.objects.filter(test_type="ssat")
        print("ssat_practice_tests: ", ssat_practice_tests)
        ssat_practice_test_list = []
        user_test_sessions = TestSession.objects.filter(user=user, test__test_type="ssat")
        completed_ssat_practice_tests_qs = user_test_sessions.filter(completed=True)
        completed_ssat_practice_tests_ids = list(completed_ssat_practice_tests_qs.values_list("test_id", flat=True))

        started_ssat_practice_tests_qs = user_test_sessions.filter(started=True)
        started_ssat_practice_tests_ids = list(started_ssat_practice_tests_qs.values_list("test_id", flat=True))

        print("completed_ssat_practice_tests_ids: ", completed_ssat_practice_tests_ids)

        # test_sessions_completed = list(TestSession.objects.filter(user=user, test__id__in=completed_ssat_practice_tests_ids).values_list("test_id", flat=True))
        # test_sessions_started = completed_ssat_practice_tests_qs.values_list("test_id", flat=True))
        # print("test_sessions_completed: ", test_sessions_completed)


        for ssat_practice_test in ssat_practice_tests:
            if ssat_practice_test.question_set.all().count() > 0 and ssat_practice_test.test_type == "ssat":
                if ssat_practice_test.id in completed_ssat_practice_tests_ids:
                    print("IN")
                    test_status = "completed"
                    test_session = completed_ssat_practice_tests_qs.get(test__id=ssat_practice_test.id)
                else:
                    if ssat_practice_test.id in started_ssat_practice_tests_ids:
                        print("IN")
                        test_status = "started"
                        test_session = started_ssat_practice_tests_qs.filter(test__id=ssat_practice_test.id)
                    else:
                        print("OUT")
                        test_status = "not started"
                        test_session = None

                ssat_practice_test_list.append({
                    "practice_test": ssat_practice_test,
                    "test_status": test_status,
                    "test_session": test_session
                    })

        print("ssat_practice_tests: ", ssat_practice_tests)
        print("ssat_practice_test_list***: ", ssat_practice_test_list)

        instructor = user_type_profile.instructor
        print("Instructor: ", instructor)
        test_type = user_type_profile.prep_for_test_type
        print("test_type??????: ", test_type)

        student_id = user_type_profile.id

        assignments = Assignment.objects.filter(instructor=instructor, student=user_type_profile)

        incomplete_assignments = assignments.filter(completed=False)
        completed_assignments = assignments.filter(completed=True)

        context = {
            "ssat_practice_test_list": ssat_practice_test_list,
            "profile_type": user_profile.user_type,
            "instructor": instructor,
            "test_type": test_type,
            "incomplete_assignments": incomplete_assignments,
            "completed_assignments": completed_assignments,
            "student_id": student_id
        }
        print("context: ", context)
        return render(request, "ace_it_test_prep/account_home.html", context)

    elif user_type == "Parent":
        pass
    elif user_type == "Instructor":
        students = Student.objects.filter(instructor=user_type_profile)
        context = {
            "profile_type": user_profile.user_type,
            "students": students
        }
        return render(request, "ace_it_test_prep/instructor_home.html", context)

def student_profile(request, student_id):
    student = Student.objects.get(id=student_id)
    # print("student: ", student.values())
    instructor = Instructor.objects.get(user_profile__user=request.user)
    tests = Test.objects.filter(test_type=student.prep_for_test_type.lower())
    assigned_tests = []
    completed_tests = []
    for test in tests:
        assignments = test.assignment_set.filter(student=student, instructor=instructor)
        for assignment in assignments:
            if assignment.completed:
                completed_tests.append(assignment)
            else:
                assigned_tests.append(assignment)
    print("assigned_tests: ", assigned_tests)
    print("completed_tests: ", completed_tests)
    context = {
        "student": student,
        "tests": tests,
        "assigned_tests": assigned_tests,
        "completed_tests": completed_tests
    }

    ##Should there be a model for assignments from instructor to student?##
    return render(request, "ace_it_test_prep/student_profile.html", context)

def assign_to_student(request, test_id, student_id):
    print("test_id: ", test_id)
    print("student_id: ", student_id)
    student = Student.objects.get(id=student_id)
    test = Test.objects.get(id=test_id)
    context = {
        "student": student,
        "test": test
    }
    return render(request, "ace_it_test_prep/assign_to_student.html", context)

def save_new_assignment(request):
    student_id = request.POST.get("student_id")
    test_id = request.POST.get("test_id")
    due_date = request.POST.get("due_date")
    instructor = Instructor.objects.get(user_profile__user=request.user)
    student = Student.objects.get(id=student_id)
    test = Test.objects.get(id=test_id)
    new_assignment = Assignment(instructor=instructor, student=student, test=test, due_date=due_date)
    new_assignment.save()
    return redirect("ace_it_test_prep:student_profile", student_id=student_id)

def add_student(request):
    return render(request, "ace_it_test_prep/add_student.html")

def invite_student(request):
    student_email = request.POST.get('student_email')
    student_user = User.objects.get(email=student_email)
    student = Student.objects.get(user_profile__user=student_user)
    instructor = Instructor.objects.get(user_profile__user = request.user)
    student.instructor = instructor
    student.save()
    print("instructor: ", instructor)
    instructor_student_list = Student.objects.filter(instructor=instructor)
    print("student: ", student)
    print("instructor_student_list: ", instructor_student_list)
    return HttpResponse("Success")


def reading_practice_overview(request):
    return render(request, "ace_it_test_prep/reading_practice_overview.html")

def verbal_practice_overview(request):
    return render(request, "ace_it_test_prep/verbal_practice_overview.html")

def vocabulary_practice(request):
    vocabulary_terms = VocabularyTerm.objects.all()
    num_terms = vocabulary_terms.count()
    id_list = []
    for i in range(0,5):
        id_list.append(random.randint(1,num_terms))
    practice_terms = vocabulary_terms.filter(id__in=id_list)
    practice_terms_serialized = serializers.serialize("json", practice_terms)

    context = {
        "first_term": practice_terms[0],
        "serialized_data": practice_terms_serialized
    }
    print("practice_terms: ", practice_terms)
    return render(request, "ace_it_test_prep/vocabulary_practice.html", context)

def test_synonyms(request):
    print("data: ", request.POST.get("serialized_data"))
    test_synonyms_data = json.loads(request.POST.get("serialized_data"))
    all_vocabulary_terms = VocabularyTerm.objects.all()
    all_vocabulary_terms_count = all_vocabulary_terms.count()
    all_terms = []
    all_terms_serialized = []
    term_data = []
    for tested_term in test_synonyms_data:
        print(tested_term)
        print("\n")
        tested_term_id = tested_term["pk"]
        distractor_ids = []
        for i in range(0,4):
            distractor_id = random.randint(0, all_vocabulary_terms_count)
            while distractor_id == tested_term_id:
                distractor_id = random.randint(0, all_vocabulary_terms_count)
            distractor_ids.append(distractor_id)

        answer_options_list = list(all_vocabulary_terms.filter(id__in=distractor_ids).values_list("term", flat=True))

        correct_answer_index = random.randint(0,4)
        for index in range(0,5):
            if index == correct_answer_index:
                synonym_index = random.randint(0,2)
                possible_correct_answers = all_vocabulary_terms.filter(id=tested_term_id).values_list("synonyms_list", flat=True)[0].split(", ")
                answer_options_list.insert(index, possible_correct_answers[synonym_index].strip(" ").capitalize())

        print("answer_options_list$$$: ", answer_options_list)
        print("answer_options_list: ", type(answer_options_list))

        tested_term_and_distractor_ids = []
        tested_term_and_distractor_ids.append(tested_term_id)
        tested_term_and_distractor_ids.extend(distractor_ids)
        random.shuffle(tested_term_and_distractor_ids)
        print("tested_term_and_distractor_ids: ", tested_term_and_distractor_ids)

        distractor_qs = all_vocabulary_terms.filter(id__in=distractor_ids)
        distractor_serialized = serializers.serialize("json", distractor_qs)

        distractor_list = []
        for distractor in distractor_qs:
            print(distractor)
            distractor_list.append({
                "term": distractor.term,
                "correct": False
            })

        # tested_term_synonyms_list = tested_term["fields"]["synonyms_list"].join(",")
        # random.shuffle(tested_term_synonyms_list)
        #
        # distractor_list.extend({
        #     "term": tested_term_synonyms_list[0],
        #     "correct": True
        # })

        term_data = {
            "tested_term": tested_term["fields"]["term"],
            "answer_options_list": answer_options_list,
            "correct_answer_index": correct_answer_index
        }

        term_data_serialized = {
            "tested_term": tested_term["fields"],
            "distractors": distractor_serialized
        }

        all_terms_serialized.append(term_data_serialized)
        all_terms.append(term_data)
    print("all_terms: ", all_terms[0])
    print("all_terms type: ", type(all_terms[0]))
    context = {
        # "tested_term": tested_term["fields"]["term"],
        # "first_term_data": json.loads(term_data[0]),
        # "term_data_json": json.dumps(term_data)
        "term_data": all_terms,
        "term_data_json": json.dumps(all_terms),
        # "term_data_json": json.dumps(all_terms_serialized)
    }
    return render(request, "ace_it_test_prep/practice_synonyms.html", context)

def score_synonyms_practice(request):
    user_answer_selections = request.POST.get("user_answer_selections").split(",")
    term_data = request.POST.get("term_data")
    jsonified = term_data.replace("\'", "\"")
    term_data = json.loads(request.POST.get("term_data").replace("\'", "\""))
    term_data_results = term_data

    index = 0
    score = 0
    for term in term_data:
        print("term: ", term)
        if term["correct_answer_index"] == user_answer_selections[index]:
            score += 1
        term_data_results[index]["user_answer_selection"] = user_answer_selections[index]

    context = {
        "term_data_results": term_data_results,
        "score": score
    }

    print("contex: ", context)
    return render(request, "ace_it_test_prep/synonyms_practice_results.html", context)

def math_practice_overview(request):
    return render(request, "ace_it_test_prep/math_practice_overview.html")

def get_sections_data(sections, test_session):
    sections_data = []
    # if test_session.count() > 0:
    #     test_session = test_session[0]
    user_test_session_sections = TestSessionSection.objects.filter(test_session=test_session, completed=True).values_list("section__name", flat=True)
    test_session_id = test_session.id
    print("user_test_session_sections: ", user_test_session_sections)
    for section in sections:
        print("section: ", section)
        if section in user_test_session_sections:
            sections_data.append({"section":section, "completed":True})
        else:
            sections_data.append({"section":section, "completed":False})
    # else:
        # test_session_id = ""
        # for section in sections:
        #     sections_data.append({"section":section, "completed":False})

    return sections_data, test_session_id


def practice_test_detail(request, test_id, student_id):
    print("PRACTICE TEST DETAIL")

    test = Test.objects.filter(id=test_id)[0]

    user_profile = UserProfile.objects.get(user=request.user)

    print("user_profile.user_type: ", user_profile.user_type)
    if user_profile.user_type == "student":
        print("Student")
        test_session, created = TestSession.objects.get_or_create(user=request.user, test=test)
        print("created: ", created)
        print("test_session: ", test_session)
        # if not created:
        #     test_session = test_session[0]
    elif user_profile.user_type == "instructor":
        print("Instructor")
        student_user = Student.objects.get(id=student_id)
        test_session = TestSession.objects.get(user=student_user.user_profile.user, test__id=test_id)


    if created:
        # test_session.started = True
        all_questions = Question.objects.filter(test=test_session.test)
        create_answer_responses(test_session, all_questions)

    sections = Section.objects.filter(test_type=test.test_type).values_list("name", flat=True).order_by("rank")
    sections_data = []

    sections_data, test_session_id = get_sections_data(sections, test_session)

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

    print("test_session: ", test_session)

    context = {
        "test_id": test_id,
        "test_session_id": test_session_id,
        "sections_data": sections_data,
        "user": test_session.user
    }
    print("context: ", context)
    return render(request, "ace_it_test_prep/practice_test_detail.html", context)

def practice_test_start_page(request, id, section):
    print("id: ", id)
    print("section: ", section)
    context = {
        "test_id": id,
        "section": section
    }
    return render(request, "ace_it_test_prep/practice_test_start_page.html", context)

def practice_test(request, test_id, section):
    print("PRACTICE TEST")
    print("test_id: ", test_id)
    print("section: ", section)
    test = Test.objects.get(id=test_id)
    section=Section.objects.get(name=section)
    test_session, session_created = TestSession.objects.get_or_create(user=request.user, test=test)
    test_session_section, session_section_created = TestSessionSection.objects.get_or_create(
        test_session=test_session,
        section=section,
        # start_date=,
        # end_date=,
        started=True
    )

    all_questions = Question.objects.filter(test=test_session.test).order_by("number")
    section_questions = all_questions.filter(section=section)
    section_questions_num = section_questions.count()
    print("section_questions: ", section_questions)
    print("questions.values_list('id', flat=True): ", list(section_questions.values_list('id', flat=True)))
    passage_ids = list(section_questions.values_list('passage__id', flat=True))
    print("passage_ids: ", passage_ids, " passage_ids_type: ", type(passage_ids))
    passages = ReadingPassage.objects.filter(id__in=passage_ids)
    print("passages: ", passages)

    #moved to practice_test_detail
    # if session_created:
    #     # test_session.started = True
    #     create_answer_responses(test_session, all_questions)

    data = get_answers(section_questions)
    # print("data[0]: ", data[0])

    assignments = Assignment.objects.filter(student__user_profile__user=request.user)

    if assignments.filter(test=test).exists():
        assignment = assignments.filter(test=test).first()
        new_assignmentsession, assignmentsession_created = AssignmentSession.objects.get_or_create(assignment=assignments.filter(test=test).first(), test_session=test_session)
        if assignmentsession_created:
            new_assignmentsession.save()
            assignment.started = True
            assignment.save()


    print("data: ", data)
    context = {
        "test_session_id": test_session.id,
        "data": data,
        "question_nums_range": range(section_questions_num),
        "question_nums": section_questions_num,
        "section": section,
        "passages": passages,
        "time_limit": section.time_limit
    }

    # print("pratice_test context: ", context)

    return render(request, "ace_it_test_prep/practice_test.html", context)

def get_answers(questions):
    data = []
    if isinstance(questions, QuerySet):
        for question in questions:
            answers_list = format_answers(question.answer_set.all())
            data.append({ "question": model_to_dict(question), "answers": answers_list })
    else:
        answers_list = format_answers(questions.answer_set.all())
        data.append({ "question": model_to_dict(questions), "answers": answers_list })
    return data

def format_answers(answers):
    answers_list = []
    for answer in answers:
        answers_list.append(model_to_dict(answer))
    return answers_list

# def create_test_session(user, test):
#     print("create_test_session")
#     test_session = TestSession()
#     test_session.user = user
#     test_session.test = test
#     test_session.save()
#     return test_session

def create_answer_responses(test_session, questions):
    count = 0
    for question in questions:
        test_response = TestResponse(session=test_session, question=question)
        test_response.save()
        count += 1

    print("COUNT: ", count)

def save_test_response(request, question_id):
    print("SAVING")
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    print("body: ", body)
    question_index = body['index'] + 1
    user_response = body['response']
    session_id = body['session_id']
    question_id = body['question_id']
    print("user_response: ", user_response)
    print("request.user: ", request.user)
    print("!!!question_id!!!: ", question_id)
    print("!!!session_id!!!: ", session_id)
    # session=TestSession.objects.get(id=session_id)
    # print("session: ", session)
    session_test_responses = TestResponse.objects.filter(session__id=session_id)
    print("session_test_responses: ", session_test_responses)
    test_response = TestResponse.objects.get(session__id=session_id, question__id=question_id)
    # test_response = TestResponse.objects.filter(session=session).filter(question__number=question_index)
    print("test_response**: ", test_response)
    # print("test_responseA: ", test_response.response)
    # print("user_response: ", user_response)
    test_response.response = user_response
    test_response.save()
    question = Question.objects.get(id=question_id)
    print("question: ", question.question_text)
    print("test_responseB: ", test_response.response)
    print("test_responseB: ", test_response.question.id)
    return JsonResponse({"message": "success"})

def get_question(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    print("body['test_session_id']: ", body['test_session_id'])
    print("body['questionNum']: ", body['questionNum'])
    test_session = TestSession.objects.get(id=body['test_session_id'])

    qs = Question.objects.filter(test=test_session.test)
    nums = qs.count()
    create_answer_responses(test_session, qs)

    data_list = []

    for question in qs:
        answers = question.answer_set.all()
        data_list.append({
            "question": json.loads(question),
            "answers": json.loads(answers)
        })

    print("DATA_LIST: ", data_list)

    first_question = Question.objects.get(test=test_session.test, number=body['questionNum'])
    # first_question_answers = Answer.objects.all()
    first_question_answers = first_question.answer_set.all()
    # first_question_serialized = serializers.serialize("json", first_question)
    first_question_answers_serialized = serializers.serialize("json", first_question_answers)
    print("first_question: ", first_question)
    print("first_question_answers: ", first_question_answers)
    data = {
        "nums": nums,
        "first_question": model_to_dict(first_question),
        "first_question_answers": first_question_answers_serialized
    }
    print("DATA: ", data)
    return JsonResponse(data, content_type='application/json')

def get_questions(request):
    print("************GETQUESTIONS")
    print("request: ", request)
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    print("body['test_session_id']: ", body['test_session_id'])
    test_session_id = body['test_session_id']
    section = body['section']
    print("section: ", section)
    test_session = TestSession.objects.get(id=test_session_id)
    # test_session = TestSession.objects.get(user=request.user, test=test)
    passages = ReadingPassage.objects.filter(test=test_session.test)

    questions = Question.objects.filter(test=test_session.test, section=section).extra({'number_int': "CAST(number as INTEGER)"}).order_by('number_int')
    data = get_answers(questions)

    nums = questions.count()

    context = {
        "test_session_id": test_session.id,
        "data": data,
        "nums": nums,
        "passages": serializers.serialize("json", passages)
    }

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

    return JsonResponse(context, content_type='application/json')

def group_answers(qs, ans):
    ans_list = []
    q_id = qs[0].id
    index = 0
    for question in qs:
        print("GSDAGAGA: ", type(ans.filter(question__id=question.id)))
        ans_list.append(ans.filter(question__id=question.id))
        index += 1
    return ans_list

def score_test(test_session_id):
    user_answers = TestResponse.objects.filter(session=test_session_id).order_by('question__id')
    for user_answer in user_answers:
        if int(user_answer.response) == int(user_answer.question.correct_answer):
            print("correct!")
            user_answer.correct = True
            user_answer.answered = True
        elif int(user_answer.response) != -1:
            print("incorrect!")
            user_answer.correct = False
            user_answer.answered = True
        user_answer.save()
    return

def submit_section(request):
    test_session_id = request.POST.get("test_session_id")
    section = request.POST.get("section")
    test_session = TestSession.objects.get(id=test_session_id)
    test_session_sections = test_session.testsessionsection_set.all()
    test_session_section = test_session_sections.get(section__name=section)
    test_session_section.completed = True
    test_session_section.save()

    student_id = Student.objects.get(user_profile__user=test_session.user)

    sections_completed = test_session_sections.values_list("completed", flat=True)

    print("sections_completed: ", sections_completed)
    # print("test_session_section.values: ", test_session_section.values())

    if sections_completed.count() == 4 and False not in sections_completed:
        print("TRUE")
        test_session.completed =  True
        test_session.save()
        assignmentsession = test_session.assignmentsession_set.first()
        print("assignmentsession: ", assignmentsession.assignment)
        assignment = assignmentsession.assignment
        assignment.completed = True
        assignment.save()

    print("test_session_section: ", test_session_section.completed)

    # user_answers = TestResponse.objects.filter(session=test_session_id).order_by('question__id')
    # user_answers_serialized = serializers.serialize("json", user_answers, fields=('question', 'response'))
    score_test(test_session_id)
    # return render(request, "ace_it_test_prep/practice_test_detail.html")
    # will redirect to practice detail page until test is complete when page will redirect
    # to results page

    print("test_session.completed: ", test_session.completed)

    if test_session.completed:
        print("session completed")
        return redirect('ace_it_test_prep:practice_test_results_overview', test_session_id=test_session_id)
    else:
        return redirect('ace_it_test_prep:practice_test_detail', test_id=test_session.test.id, student_id=student_id)

    # return redirect('ace_it_test_prep:practice_test_detail', test_id=test_session.test.id)

def practice_test_results_overview(request, test_session_id):
    print("practice_test_results_overview")
    test_session = TestSession.objects.get(id=test_session_id)
    print("test_session!!!!: ", test_session)
    test = test_session.test
    sections = Section.objects.filter(test_type=test.test_type).values_list("name", flat=True).order_by("rank")
    print("section")
    sections_data = []

    sections_data, test_session_id = get_sections_data(sections, test_session)

    student_user_profile = UserProfile.objects.get(user=test_session.user)
    student_id = Student.objects.get(user_profile=student_user_profile)

    context = {
        "test_id": test.id,
        "test_session_id": test_session.id,
        "sections_data": sections_data,
        "user": test_session.user,
        "student_id": student_id
    }
    # print("context: ", context)
    # return render(request, "ace_it_test_prep/practice_test_results_overview.html", context)

    if test_session.completed:
        print("session completed")
        return render(request, 'ace_it_test_prep/practice_test_results_overview.html', context)
    else:
        return render(request, 'ace_it_test_prep/practice_test_detail.html', context)



def practice_test_results(request, test_session_id, section=None):
    print("SECTION: ", section)
    print("test_session_id$$$$$ ", test_session_id)
    print("test_session_id$$$$$ ", type(test_session_id))
    test_session = TestSession.objects.get(id = test_session_id)
    questions = Question.objects.filter(test = test_session.test, section=section).extra({'number_int': "CAST(number as INTEGER)"}).order_by('number_int')
    question_ids = questions.values_list("id", flat=True)
    print(question_ids)
    # user_answers = questions.testresponse_set.all()
    user_answers = TestResponse.objects.filter(session=test_session, question__id__in = question_ids).order_by('question__number')
    # for question in questions:
    #     user_answers.append(TestResponse.objects.filter(question = question))
    # user_answers = TestResponse.objects.filter(session__id = test_session_id)
    test_id = test_session.test.id
    # print("user_answers!!!: ", user_answers.count())
    print("user_answers!!!: ", user_answers)
    print("all_questions!!!: ", questions)
    # print("questions@@@: ", user_answers[0].correct)
    # print("questions&&&: ", user_answers[1].correct)
    print(questions[0].__dict__)
    print("question 1: ",questions[0])
    zipped_data = zip(user_answers, questions)
    # context = {
    #     'user_answers': user_answers,
    #     'questions': questions
    # }

    user_profile = UserProfile.objects.get(user=request.user)

    print("user_profile: ", user_profile.user_type)

    if user_profile.user_type == "student":
        student = Student.objects.get(user_profile=user_profile)
    elif user_profile.user_type == "instructor":
        student = Student.objects.get(user_profile__user=test_session.user)

    print("student: ", student.user_profile.user.first_name)

    data = {
        'zipped_data': zipped_data,
        "test_session_id": test_session.id,
        "test_id": test_id,
        "student": student
    }
    # for ans, q in zipped_data:
    #     print("question_id: ", q.id, "question_text: ", q.question_text)
    #     print("answer_question_id: ", ans.question.id, "answer.response: ", ans.response)

    # print("zipped_data09090909: ", zipped_data[0])
    # print("zipped_data09090909: ", zipped_data.questions)
    return render(request, "ace_it_test_prep/practice_test_results.html", data)

def practice_test_results_detail_view(request):
    print("DETAILS")
    # test_id = request.POST.get("test_id")
    # print("test_id: ", test_id)
    # print("test_id TYPE: ", type(test_id))
    test_response_id = request.POST.get("test_response_id")
    section = request.POST.get("section")
    print("test_response_id: ", test_response_id)
    test_response = TestResponse.objects.get(id=test_response_id)
    test_session_id = test_response.session.id
    action = request.POST.get('action')
    # question_id = request.POST.get("question_id")
    question_id = test_response.question.id
    print("question_id: ", question_id)
    current_question = Question.objects.get(id=question_id)
    # question_number = int(current_question.number)
    # print("question_numberA: ", question_number)
    questions = Question.objects.filter(test = current_question.test, section=current_question.section)
    num_of_questions = questions.count()
    # # print("questions: ", num_of_questions)
    if action == "next":
        print("NEXT")
        next_number = int(current_question.number) + 1
        # # print("next_number: ", next_number)

        if next_number > num_of_questions:
            next_number = 1

        next_question = questions.get(number = next_number)
        current_question = next_question
        test_response = TestResponse.objects.get(session__user=request.user, question=current_question)
    elif action == "back":
        print("BACK")
        next_number = int(current_question.number) - 1
        if next_number == 0:
            next_number = num_of_questions
        next_question = questions.get(number = next_number)
        current_question = next_question
        test_response = TestResponse.objects.get(session__user=request.user, question=current_question)
    # print("question_numberB: ", question_number)
    # question = questions.get(number = question_number, test = test_response.session.test)
    # print("PPPPP: ", test_session_id)
    # print("PPPPP: ", question)
    # test_response = TestResponse.objects.filter(session_id=test_session_id, question=question).first()
    # print("test_response: ", test_response)
    # test_response_id = test_response.id
    answers = current_question.answer_set.all()
    answers_list = []
    print("answers: ", answers)
    for answer in answers:
        answers_list.append(model_to_dict(answer))

    print("answers_list******: ", answers_list)



    context = {
        "test_response": test_response,
        "question": current_question,
        "answers": answers,
        "test_session_id": test_session_id
    }

    print("CONTEXT: ", context)
    return render(request, "ace_it_test_prep/practice_test_results_detail_view.html", context)
