from django.urls import path

from . import views

print("URLS")

app_name = 'ace_it_test_prep'
urlpatterns = [
    path('', views.index, name='index'),
    path('signup', views.signup, name='signup'),
    path('login_user', views.login_user, name='login_user'),
    path('logout_user', views.logout_user, name='logout_user'),
    path('account_home', views.account_home, name='account_home'),
    path('account_home/<profile_type>', views.account_home, name='account_home'),
    path('get_questions', views.get_questions, name='get_questions'),
    path('practice_test/<question_id>/save_test_response', views.save_test_response, name='save_test_response'),
    path('practice_test/<test_id>/<section>', views.practice_test, name='practice_test'),
    path('practice_test_detail/<test_id>/<student_id>', views.practice_test_detail, name='practice_test_detail'),
    path('practice_test_start_page/<id>/<section>', views.practice_test_start_page, name='practice_test_start_page'),

    path('practice_test_results/<test_session_id>', views.practice_test_results, name='practice_test_results'),
    path('practice_test_results/<test_session_id>/<section>', views.practice_test_results, name='practice_test_results'),
    path('practice_test_results_overview/<test_session_id>', views.practice_test_results_overview, name='practice_test_results_overview'),
    path('submit_section', views.submit_section, name='submit_section'),
    path('get_question', views.get_question, name='get_question'),
    path('save_test_response', views.save_test_response, name='save_test_response'),
    path('practice_test_results_detail_view', views.practice_test_results_detail_view, name='practice_test_results_detail_view'),
    path('reading_practice_overview', views.reading_practice_overview, name='reading_practice_overview'),
    path('math_practice_overview', views.math_practice_overview, name='math_practice_overview'),
    path('verbal_practice_overview', views.verbal_practice_overview, name='verbal_practice_overview'),
    path('upload_TI_Quizlet_Terms', views.upload_TI_Quizlet_Terms, name='upload_TI_Quizlet_Terms'),
    path('uploads', views.uploads, name='uploads'),
    path('vocabulary_practice', views.vocabulary_practice, name='vocabulary_practice'),
    path('vocabulary_roots_practice', views.vocabulary_roots_practice, name='vocabulary_roots_practice'),
    path('vocabulary_roots_practice/<root>', views.vocabulary_roots_practice, name='vocabulary_roots_practice'),
    path('vocabulary_roots_practice_synonyms', views.vocabulary_roots_practice_synonyms, name='vocabulary_roots_practice_synonyms'),
    
    path('test_synonyms', views.test_synonyms, name='test_synonyms'),
    path('score_synonyms_practice', views.score_synonyms_practice, name='score_synonyms_practice'),
    path('add_student', views.add_student, name='add_student'),
    path('invite_student', views.invite_student, name='invite_student'),
    path('student_profile/<student_id>', views.student_profile, name='student_profile'),
    path('assign_to_student/<test_id>/<student_id>', views.assign_to_student, name='assign_to_student'),
    path('save_new_assignment', views.save_new_assignment, name='save_new_assignment'),
    path('mcq_submit_section', views.mcq_submit_section, name='mcq_submit_section'),
    path('mcq_results_detail', views.mcq_results_detail, name='mcq_results_detail'),
    path('vocabulary_by_category', views.vocabulary_by_category, name='vocabulary_by_category'),
    path('vocabulary_by_category/<category>', views.vocabulary_by_category, name='vocabulary_by_category'),
    path('vocabulary_flashcards_overview', views.vocabulary_flashcards_overview, name='vocabulary_flashcards_overview'),
    path('vocabulary_derivatives_practice', views.vocabulary_derivatives_practice, name='vocabulary_derivatives_practice'),
     path('vocabulary_derivatives_practice/<root>', views.vocabulary_derivatives_practice, name='vocabulary_derivatives_practice'),
]