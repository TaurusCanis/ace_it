from django.core.management.base import BaseCommand
from ace_it_test_prep.models import *
import json

class Command( BaseCommand):
#This can be used to take in an absolute path to file
    # def add_arguments(self, parser):
    #     parser.add_argument('json_file', type=str)


    def handle( self, *args, **options ):
        # use commented line below if taking in absolute path
        # with open(options['json_file'], 'r') as json_file:
        with open('ace_it_test_prep/management/commands/SSAT_Practice_Test_1_Official.json', 'r') as json_file:
        	json_data = json_file.read()

        json_data_dict = json.loads(json_data)

        new_test = Test(test_type="ssat", name=json_data_dict["initData"]["name"])
        new_test.save()

        questions = json_data_dict["initData"]["questions"]

        questions_list = []
        question_index = 0

        for question in questions:
            print(question["stimulus"])
            new_question = Question()
            new_question.test = new_test

            if question_index < 25:
                new_question.section = "math_1"
                new_question.number = question_index + 1
            elif question_index >= 25 and question_index < 65:
                new_question.section = "reading"
                new_question.number = 25 - (question_index + 1)
            elif question_index >= 65 and question_index < 125:
                new_question.section = "verbal"
                new_question.number = 65 - (question_index + 1)
            else:
                new_question.section = "math_2"
                new_question.number = 125 - (question_index + 1)

            new_question.question_text = question["stimulus"]
            new_question.difficulty = question["difficulty"]
            new_question.primary_topic = question["topics"]["primary"]
            new_question.secondary_topic = question["topics"]["secondary"]
            new_question.correct_answer = question["validation"]["valid_response"]["value"][0]
            correct_answer_index = question["validation"]["valid_response"]["value"]
            new_question.save()
            # questions_list.append(question_text)
            answers = question["options"]

            answer_index = 0
            for answer in answers:
                new_answer = Answer()
                new_answer.question = new_question
                new_answer.value = answer["value"]
                new_answer.option = answer["label"]
                new_answer.explanation = question["metadata"]["distractor_rationale_response_level"][answer_index]
                answer_index += 1
                new_answer.save()


            # distractors = question["metadata"]["distractor_rationale_response_level"]
            # print(index)

            question_index += 1


        # print(len(questions_list))
