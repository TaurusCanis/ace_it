from question_maker.models import Word, Definition
import json, requests
from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):

    def handle(self, *args, **options):
        def get_similar_spellings(word):
            url_sp = 'https://api.datamuse.com/words?sp=' + word
            print("get_similar_spellings")
            return [value['word'] for value in json.loads(requests.request("GET", url_sp).text)]

        def get_similar_sounds(word):
            url_sl = 'https://api.datamuse.com/words?sl=' + word
            print("get_similar_sounds")
            return [value['word'] for value in json.loads(requests.request("GET", url_sl).text)]

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

        with open("ace_it_test_prep/SSAT2000_full_dictionary_2.json") as file:
            data = json.load(file)

        print("DATA LENGTH: ", len(data))

        index = 387
        for word in data[index:]:
            print("Word Index: ", index)
            word_data = json.loads(word)
            word = word_data["word"]
            print("word_data: ", word_data)
            print("WORD[WORD]: ", word)
            new_word = Word()
            new_word.word = word
            new_word.similar_spellings = get_similar_spellings(word)
            new_word.similar_sounds = get_similar_sounds(word)
            new_word.theme_relations = get_theme_relations(word)
            #The above two were never saved. This needs to be run again for these two.
            new_word.associations = get_associations(word)
            new_word.save()

            try:
                for result in word_data["results"]:
                    new_definition = Definition()
                    new_definition.word = new_word
                    new_definition.save()
                    #This did not work because the keys for result are not the same as the model field names. Change models field names?
                    for key, value in result.items():
                        setattr(new_definition, key, value)
                        new_definition.save()
            except:
                index += 1
                continue
            index += 1
