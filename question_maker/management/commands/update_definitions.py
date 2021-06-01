from question_maker.models import Word, Definition
import json, requests
from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    
    def handle(self, *args, **options):
        def get_theme_relations(word):
            url = "https://twinword-word-graph-dictionary.p.rapidapi.com/theme/"

            querystring = {"entry":word}

            headers = {
                'x-rapidapi-key': "5d633d11f3mshee22825861d1068p13d37cjsnc0266c59c324",
                'x-rapidapi-host': "twinword-word-graph-dictionary.p.rapidapi.com"
                }

            response_themes = json.loads(requests.request("GET", url, headers=headers, params=querystring).text)
            
            print("get_theme_relations")
            
            if response_themes["result_msg"] == "Success":
                return response_themes["theme"]
            else:
                return None
            

        def get_associations(word):
            url = "https://twinword-word-associations-v1.p.rapidapi.com/associations/"

            querystring = {"entry":word}

            headers = {
                'x-rapidapi-key': "5d633d11f3mshee22825861d1068p13d37cjsnc0266c59c324",
                'x-rapidapi-host': "twinword-word-associations-v1.p.rapidapi.com"
                }

            response_associations = json.loads(requests.request("GET", url, headers=headers, params=querystring).text)
            
            print("get_associations")
            
            if response_associations["result_msg"] == "Success":
                return response_associations["associations_array"]
            else:
                return None
        
        def add_api_data():
            words = Word.objects.all()
            index = 0
            for word in words:
                word.theme_relations = get_theme_relations(word)
                word.associations = get_associations(word)
                word.save()
                index += 1
                
#        with open("ace_it_test_prep/SSAT2000_full_dictionary_2.json") as file:
        #            data = json.load(file)
        
#        def add_json_file_data():
#            index = 0
#            for word in data[index:]:
#                word_data = json.loads(word)
#                word = word_data["word"]
#
#                try:
#    #                print("TRY")
#                    definitions = Definition.objects.filter(word__word=word)
#                    count_index = 0
#                    for definition in definitions:
#                        result = word_data["results"][count_index]
#                        for key, value in result.items():
#                            print("definition: ", definition)
#                            print("key: ", key)
#                            print("value: ", value)
#                            setattr(definition, key, value)
#                            definition.save()
#                        count_index += 1
#                except:
#                    index += 1
#                    continue
#                index += 1
                
        add_api_data()
