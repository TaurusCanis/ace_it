from django.urls import path

from . import views

print("URLS")

app_name = 'question_maker'
urlpatterns = [
    path('', views.index, name='index'),
    path('verbal_questions', views.verbal_questions, name='verbal_questions'),
    path('math_questions', views.math_questions, name='math_questions'),
    path('reading_questions', views.reading_questions, name='reading_questions'),
    path('synonyms_questions', views.synonyms_questions, name='synonyms_questions'),
    path('analogies_questions', views.analogies_questions, name='analogies_questions'),
    path('create_synonym_question_view', views.create_synonym_question_view, name='create_synonym_question_view'),
    path('synonyms_view', views.synonyms_view, name='synonyms_view'),
    path('update_synonym/<synonym_id>', views.update_synonym, name='update_synonym'),
    path('update_synonym', views.update_synonym, name='update_synonym'),
    path('get_random_word', views.get_random_word, name='get_random_word'),
    path('delete_synonym/<synonym_id>', views.delete_synonym, name='delete_synonym'),
    path('update_synonym_explanations', views.update_synonym_explanations, name='update_synonym_explanations'),
    path('update_synonym_explanations/<synonym_id>', views.update_synonym_explanations, name='update_synonym_explanations'),
    path('create_analogies', views.create_analogies, name='create_analogies'),
    path('view_analogies', views.view_analogies, name='view_analogies'),
]
