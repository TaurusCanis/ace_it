from django.core.management.base import BaseCommand
from ace_it_test_prep.models import *
import json

class Command( BaseCommand):
#This can be used to take in an absolute path to file
    # def add_arguments(self, parser):
    #     parser.add_argument('json_file', type=str)


    def handle( self, *args, **options ):
        with open('ace_it_test_prep/management/commands/SSAT_Practice_Test_1_Official.json', 'r') as json_file:
        	json_data = json_file.read()

        json_data_dict = json.loads(json_data)
        passages = json_data_dict["initData"]["features"]

        test = Test.objects.get(id=2)

        for passage in passages:
            new_passage = ReadingPassage(test=test, text=passage["content"])
            new_passage.save()
