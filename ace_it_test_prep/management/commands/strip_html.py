from django.core.management.base import BaseCommand
from ace_it_test_prep.models import *
import json
from bs4 import BeautifulSoup
import bleach

class Command( BaseCommand):
#This can be used to take in an absolute path to file
    # def add_arguments(self, parser):
    #     parser.add_argument('json_file', type=str)


    def handle( self, *args, **options ):
        # reading_passages = ReadingPassage.objects.filter(test__id=5).order_by("id")
        # index_counter = 0
        # for reading_passage in reading_passages:
        #     reading_passage.passage_index = index_counter
        #     # reading_passage.save()
        #     index_counter += 1
        #     print("ORIGINAL: ", reading_passage.text)
        #     clean = bleach.clean(reading_passage.text, tags=['p', 'strong', 'b', 'i', 'em', 'img'], strip=True)
        #     print("CLEAN: ", clean)
        #     reading_passage.text = clean 
        #     # reading_passage.save()
        #     # print(reading_passage.passage_index)

        reading_questions = Question.objects.filter(test__id=3, section='reading')
        # for question in reading_questions:
        #     print("question: ", question.question_text)
        #     clean = bleach.clean(question.question_text, tags=[], strip=True)
        #     print("CLEAN: ", clean)
        #     question.question_text = clean 
        #     question.save()

        reading_question_answer_options = Answer.objects.filter(question__in=reading_questions)
        for answer_option in reading_question_answer_options:
            print("answer_option: ", answer_option.option)
            clean = bleach.clean(answer_option.option, tags=[], strip=True)
            print("CLEAN: ", clean)
            answer_option.option = clean 
            answer_option.save()
