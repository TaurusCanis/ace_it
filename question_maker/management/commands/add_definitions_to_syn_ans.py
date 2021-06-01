from question_maker.models import Word, Definition, Synonym, SynonymAnswerOption
import json, requests, random
from django.core.management.base import BaseCommand, CommandError
from modules import create_synonym

class Command(BaseCommand):

    def handle(self, *args, **options):
        syn_ans = SynonymAnswerOption.objects.filter(definition=None)

        for synonym_answer in syn_ans:
            synonym_answer_word_value = synonym_answer.value
            has_definitions = False
            try:
                synonym_answer_word = Word.objects.get(word=synonym_answer_word_value)
                synonym_answer_definitions = Definition.objects.filter(word=synonym_answer_word)
                print("synonym_answer_definitions.count()^^^^^^^^^: ", synonym_answer_definitions.count())
                if synonym_answer_definitions.count() > 0:
                    synonym_answer_word.definition = random.choice(synonym_answer_definitions)
                    synonym_answer_word.save()
                    has_definitions = True
            except:
                synonym_answer_word = Word()
                synonym_answer_word.word = synonym_answer_word_value
                synonym_answer_word.similar_spellings = create_synonym.get_similar_spellings(synonym_answer_word_value)
                synonym_answer_word.similar_sounds = create_synonym.get_similar_sounds(synonym_answer_word_value)
                synonym_answer_word.theme_relations = create_synonym.get_theme_relations(synonym_answer_word_value)
                synonym_answer_word.associations = create_synonym.get_associations(synonym_answer_word_value)
                synonym_answer_word.save()
                # synonym_answer_word_lookup = new_synonym_answer_word

            print("has_definitions:&&&&&&&&& ", has_definitions)
            if not has_definitions:
                synonym_answer_definitions = create_synonym.get_dictionary_data(synonym_answer_word.word)
                print("synonym_answer_definitions----->>>>>>>: ", synonym_answer_definitions)
                for result in synonym_answer_definitions:
                    new_definition = Definition()
                    new_definition.word = synonym_answer_word
                    new_definition.save()
                    #This did not work because the keys for result are not the same as the model field names. Change models field names?
                    for key, value in result.items():
                        setattr(new_definition, key, value)
                        new_definition.save()
                defs = Definition.objects.filter(word=synonym_answer_word)
                print("defs: ", defs)
                random_def = random.choice(defs)
                print("random_def: }}}}}}++++ ", random_def)
                print("synonym_answer: }}}}}}++++ ", synonym_answer)
                synonym_answer.definition = random_def
                # setattr(synonym_answer_word, "definition", random_def)
                synonym_answer.save()
