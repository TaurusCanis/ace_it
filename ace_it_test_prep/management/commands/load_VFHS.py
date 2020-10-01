from django.core.management.base import BaseCommand
from ace_it_test_prep.models import *
import json

class Command( BaseCommand):
    def handle( self, *args, **options ):
        with open('ace_it_test_prep/management/commands/VFHS_Latin_prefix_terms.txt', 'r') as my_file:
            for line in my_file:
                if line != "\n":
                    new_term = {}
                    new_term["term"] = line.split(":")[0].rstrip()
                    new_term["definition"] = line.split(":")[1].rstrip()

                    # print(line.split("-")[0].rstrip())
                    # print(line.split("-")[1])


                    # new_root_term = VocabularyRoot(
                    #     root_type = "P",
                    #     term = line.split(":")[0].rstrip(),
                    #     definition = line.split(":")[1]
                    # )
                    # new_root_term.save()

                    new_vocabulary_term = VocabularyTerm(
                        term = line.split(":")[0].rstrip(),
                        definition = line.split(":")[1].rstrip()
                    )
                    new_vocabulary_term.save()


                    print(new_vocabulary_term)

