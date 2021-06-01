from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from modules import create_synonyms, create_synonym, create_word
from modules.math_qs import coordinate_geometry, algebraic_expressions_keywords, geometry_cube_dimensions
from question_maker.models import *
import random, json
from django.forms.models import model_to_dict
from django.core import serializers
from question_maker.serializers import WordSerializer, DefinitionSerializer
from rest_framework.parsers import JSONParser

# Create your views here.

def index(request):
    # word = create_synonym.get_random_word(1)
    # for key, value in model_to_dict(word).items():
    #     print(key, " - ", value)
    # definitions = create_synonym.get_definitions(word.id)
    # for definition in definitions:
    #     for key, value in model_to_dict(definition).items():
    #         print(key, " - ", value)

    return render(request, "question_maker/index.html")

def verbal_questions(request):
    return render(request, "question_maker/verbal_questions.html")

def math_questions(request):
    question_data = geometry_cube_dimensions.q_2()
    context = {
        "question": question_data["question_text"],
        "options": question_data["options"],
    }
    return render(request, "question_maker/math_q.html", context)

def reading_questions(request):
    return HttpResponse("Reading Questions")

def get_word(num_questions):
    definition_ids = Definition.objects.all().values_list("id", flat=True)
    print(definition_ids.count())
    definition_list = []
    print()
    for n in range(0, int(num_questions)):
        print(n)
        definition = Definition.objects.filter(id=random.choice(definition_ids))
        definition_list.append(definition)
    print(len(definition_list))
    return definition_list

def view_analogies(request):
    analogies = Analogy.objects.all()
    context = {
        "analogy_data": []
    }
    for analogy in analogies:
        analogy_answer_options = AnalogyAnswerOption.objects.filter(analogy=analogy)
        context["analogy_data"].append({
            "analogy": analogy,
            "analogy_answer_option": analogy_answer_options
        })

    return render(request, "question_maker/analogies_view.html", context)

def create_analogies(request):
    print("num_questions: ", request.POST.get("num_questions"))
    num_questions = request.POST.get("num_questions")
    definition_list = get_word(num_questions)
    print(len(definition_list))
    for definition in definition_list:
        analogy_pattern = random.choice(["S", "D"])
        fields = definition[0].get_field_names()
        analogy_fields = fields[4:]
        selected_field = random.choice(analogy_fields)
        field_values = getattr(definition[0], selected_field)
        field_value = field_values[random.randint(0, len(field_values) - 1)]
        word_A_definition = definition[0]
        word_B_definition = get_or_create_word(field_value)
        print("WORD_B_DEFINITION: ", word_B_definition)

        if analogy_pattern is "S":
            word_C_definition, word_D_definition = create_analogy_answer(selected_field)
            distractors = create_analogy_distractors(selected_field, word_C_definition.word.word)
            word_C = word_C_definition.word.word
            print("Question: ")
            print(word_A_definition.word.word, " is to ", word_B_definition.word.word, " as ", word_C, " is to ",)
            print("Answer Options: ")
            correct_answer = word_D_definition
            print(correct_answer)
            distractors_answer_list = []
            for tup in enumerate(distractors):
                distractors_answer_list.append(tup[1])
                print(tup[1].word)
            save_analogy(analogy_pattern, word_A_definition, word_B_definition, correct_answer, distractors_answer_list, selected_field, word_C_definition)
        else:
            answer = create_analogy_answer(selected_field)
            distractors = create_analogy_distractors(selected_field)
            print("Question: ")
            print(definition[0].word.word, " is to ", field_value)
            print("Answer options: ")
            print("as ", answer[0].word.word, " is to ", answer[1])
            correct_answer = (answer[0], answer[1])
            distractors_answer_list = []
            for tup in enumerate(distractors):
                print("TUP: ", tup)
                distractors_answer_list.append((tup[1][0], tup[1][1]))
                print(tup[1][0].word.word, " is to ", tup[1][1])
            save_analogy(analogy_pattern, word_A_definition, word_B_definition, correct_answer, distractors_answer_list, selected_field)

    return HttpResponse("create synonyms")

def save_analogy(analogy_pattern, word_A, word_B, correct_answer, distractors_answer_list, relationship, word_C=None):
    new_analogy = Analogy()
    new_analogy.pattern = analogy_pattern
    new_analogy.relationship = relationship
    new_analogy.word_A = word_A
    new_analogy.word_B = word_B
    if word_C is not None:
        new_analogy.word_C = word_C
    new_analogy.save()

    print("analogy_pattern: ", analogy_pattern)
    print("word_A: ", word_A.word.word)
    print("word_B: ", word_B.word.word)
    correct_analogy_answer_option = AnalogyAnswerOption()
    correct_analogy_answer_option.analogy = new_analogy

    if word_C:
        correct_analogy_answer_option.word_D = correct_answer
        print("word_C: ", word_C.word.word)
        print("correct_answer: ", correct_answer.word.word)
    else:
        print("correct_answer[0]: ", correct_answer[0].word.word, " ", correct_answer[1].word.word)
        correct_analogy_answer_option.word_C = correct_answer[0]
        correct_analogy_answer_option.word_D = correct_answer[1]
    correct_analogy_answer_option.is_correct = True
    correct_analogy_answer_option.save()

    for item in distractors_answer_list:
        new_analogy_answer_option = AnalogyAnswerOption()
        new_analogy_answer_option.analogy = new_analogy
        if analogy_pattern == "S":
            new_analogy_answer_option.word_D = item
        else:
            new_analogy_answer_option.word_C = item[0]
            new_analogy_answer_option.word_D = item[1]
        new_analogy_answer_option.save()
        if isinstance(item, tuple):
            print("items!!!!xxx: ", item[0].word.word, " ", item[1].word.word)
        else:
            print("item****: ", item.word.word)

    return

def get_or_create_word(word):
    word_object, word_object_created = Word.objects.get_or_create(word=word)
    print("word_object_created: ", word_object_created)
    if word_object_created:
        word_object.similar_spellings = create_word.get_similar_spellings(word_object.word)
        word_object.similar_sounds = create_word.get_similar_sounds(word_object.word)
        word_object.theme_relations = create_word.get_theme_relations(word_object.word)
        word_object.associations = create_word.get_associations(word_object.word)
        word_object.save()

    if not Definition.objects.filter(word=word_object).exists():
        create_definitions(word_object)

    return Definition.objects.filter(word=word_object).first()

def create_definitions(word):
    analogy_answer_definitions = create_synonym.get_dictionary_data(word.word)
    for result in analogy_answer_definitions:
        if result["partOfSpeech"] is None:
            continue
        new_definition = Definition()
        new_definition.word = word
        new_definition.save()
        #This did not work because the keys for result are not the same as the model field names. Change models field names?
        for key, value in result.items():
            setattr(new_definition, key, value)
            new_definition.save()


def create_analogy_answer(selected_field):
    definitions = Definition.objects.exclude(**{ selected_field: None})
    selected_definition = definitions[random.randint(0, definitions.count() - 1)]
    print("selected_field: ", selected_field, " type: ", type(selected_field))
    print("selected_definition: ", selected_definition)
    selected_field_values = getattr(selected_definition, selected_field)
    print("selected_field_values: ", selected_field_values)
    return (selected_definition, get_or_create_word(selected_field_values[random.randint(0, len(selected_field_values) - 1)]))

def create_analogy_distractors(selected_field, first_word=None):
    definitions_pks = Definition.objects.exclude(**{ selected_field: None}).values_list("id", flat=True)
    print("definitions_pks: ", definitions_pks, " type: ", type(definitions_pks))
    selected_definition_pks = random.sample(list(definitions_pks), 4)
    selected_definitions = Definition.objects.filter(id__in=selected_definition_pks)
    distractors_list = []
    for selected_definition in selected_definitions:
        fields = selected_definition.get_field_names(selected_field)[4:]
        selected_field = random.choice(fields)
        print("distractor_fields: ", fields)
        # if len(fields) == 0:
        #     get_word(1)[0].word.word
        selected_field_values = getattr(selected_definition, selected_field)
        selected_field_value = selected_field_values[random.randint(0, len(selected_field_values) - 1)]
        print("selected_field_values: ", selected_field_values)
        print("FIRST WORD: ", first_word)
        if first_word is None:
            distractors_list.append((selected_definition, get_or_create_word(selected_field_value)))
        else:
            distractors_list.append(selected_definition)
    return distractors_list

def synonyms_view(request):
    synonyms = Synonym.objects.filter(id__lte=40)
    synonyms_list = []

    for synonym in synonyms:
        definitions = Definition.objects.filter(word=synonym.word).exclude(synonyms=None)
        definition_answer_option_alternates_dict = {}
        for definition in definitions:
            for field in [f.get_attname() for f in Definition._meta.fields]:
                if getattr(definition, field) is not None:
                    print("NOT NONE")
                    if isinstance(getattr(definition, field), list) and field is not "examples":
                        if definition_answer_option_alternates_dict.get(field) is None:
                            definition_answer_option_alternates_dict[field] = []
                        print("IS LIST")
                        definition_answer_option_alternates_dict[field].extend(list(getattr(definition, field)))
                    # else:
                    #     definition_answer_option_alternates_dict[field] = getattr(definition, field)

        print("definition_answer_option_alternates_dict: ", definition_answer_option_alternates_dict)
        synonym_answer_options = SynonymAnswerOption.objects.filter(synonym=synonym)
        random_words = []
        for option in synonym_answer_options:
            word_pks = Word.objects.all().values_list('pk', flat=True)
            random_words.append(Word.objects.get(pk=random.choice(word_pks)))
        synonyms_list.append({
            "synonym": synonym,
            "synonym_answer_options": synonym_answer_options.values(),
            "random_words": random_words,
            "definition_answer_option_alternates_dict": definition_answer_option_alternates_dict,

        })
    context = {
        "synonyms_list": synonyms_list,
    }
    print("*******synonyms_list[0]['definition_answer_option_alternates_dict']: ", synonyms_list[0]["synonym_answer_options"])
    return render(request, "question_maker/synonyms_view.html", context)

def update_synonym_explanations(request):
    return

def delete_synonym(request, synonym_id):
    print("DELETE")
    synonym = Synonym.objects.get(id=synonym_id)
    synonym.delete()

    return redirect("/question_maker/update_synonym")

def get_synonym():
    # synonym = Synonym.objects.get(id=synonym_id)
    synonym = Synonym.objects.filter(has_been_vetted=False).order_by("id").first()
    synonyms_list = []
    definitions = Definition.objects.filter(word=synonym.word)
    definition_answer_option_alternates_dict = {}
    for definition in definitions:
        for field in [f.get_attname() for f in Definition._meta.fields]:
            if getattr(definition, field) is not None:
                print("NOT NONE")
                if isinstance(getattr(definition, field), list) and field is not "examples":
                    if definition_answer_option_alternates_dict.get(field) is None:
                        definition_answer_option_alternates_dict[field] = []
                    print("IS LIST")
                    definition_answer_option_alternates_dict[field].extend(list(getattr(definition, field)))
                # else:
                #     definition_answer_option_alternates_dict[field] = getattr(definition, field)

    print("definition_answer_option_alternates_dict: ", definition_answer_option_alternates_dict)
    synonym_answer_options = SynonymAnswerOption.objects.filter(synonym=synonym).order_by("id")
    random_words = []
    for option in synonym_answer_options:
        word_pks = Word.objects.all().values_list('pk', flat=True)
        random_words.append(Word.objects.get(pk=random.choice(word_pks)))
    synonyms_list.append({
        "synonym": synonym,
        "synonym_answer_options": synonym_answer_options,
        # "synonym_answer_options": synonym_answer_options.values(),
        "random_words": random_words,
        "definition_answer_option_alternates_dict": definition_answer_option_alternates_dict,

    })
    print("APPEND")
    return synonyms_list

def update_synonym_explanations(request, synonym_id=None):
    print("UPDATE EXPLANATIONS")
    synonyms_list = get_synonym()
    context = {
        "synonyms_list": synonyms_list,
    }
    print("synonyms_list: ", synonyms_list)
    return render(request, "question_maker/update_answer_explanations.html", context)

def update_synonym(request, synonym_id=None):
    print("request.method: ", request.method)


    if request.method == "POST":
        synonym_answer_options = SynonymAnswerOption.objects.filter(synonym_id=synonym_id).order_by("id")
        print(request.POST)
        synonym = Synonym.objects.get(id=synonym_id)
        if request.POST.get("has_been_vetted"):
            print("ON+++++++++++++++++__________))))))))")
            synonym.has_been_vetted = True
        else:
            synonym.has_been_vetted = False
        synonym.difficulty = request.POST.get("synonym_difficulty")
        synonym.save()

        for item in request.POST:
            if "selected-answer-option" in item:
                print("item: ", item)
                print("synonym_answer_options: ", synonym_answer_options)
                update_synonym_object = synonym_answer_options[int(item.split("_")[1]) - 1]
                print("Old answer: ", update_synonym_object.value)
                print("New answer: ", request.POST.get(item))
                update_synonym_object.value = request.POST.get(item)
                setattr(update_synonym_object, "value", request.POST.get(item))
                update_synonym_object.save()
                print("********: ", update_synonym_object)
                print(": ", update_synonym_object.value)

        # return HttpResponse("update_synonym POST")
    synonyms_list = get_synonym()
    context = {
        "synonyms_list": synonyms_list,
    }
    return render(request, "question_maker/update_synonym.html", context)

def get_random_word(request):
    print("random_word")
    pks = Word.objects.values_list('pk', flat=True)
    random_pk = random.choice(pks)
    random_word = Word.objects.get(pk=random_pk)
    print("random_word: ", random_word.word)
    response = json.dumps({ "random_word":  random_word.word })
    print("response: ", response)
    return JsonResponse({ "random_word":  random_word.word })

def create_synonym_question_view(request):
    if request.method == "POST":
        word_qs = create_synonym.get_random_word(1)
        synonym_questions = []
        for w in word_qs:
            word = w
            word_serialized = WordSerializer(word).data
            print("word_serialized: ", word_serialized)
            print("******************")
            word_data = serializers.serialize('python', word_qs, ensure_ascii=False)
            print("word_data: ", word_data)
            # word_data = serializers.serialize("python", word)
            definitions = create_synonym.get_definitions(word.id)
            definitions_serialized = DefinitionSerializer(definitions, many=True).data
            definitions_data = serializers.serialize('python', definitions, ensure_ascii=False)
            # suggested_definition = random.choice(definitions)
            suggested_definition = random.choice(definitions.exclude(synonyms=None))
            suggested_definition_data = serializers.serialize('json', [suggested_definition])
            print("suggested_definition: ", suggested_definition)
            serialized_definition_manual = {}
            for field in [f.get_attname() for f in Definition._meta.fields]:
                if getattr(suggested_definition, field) is not None:
                    if type(getattr(suggested_definition, field)) is "list":
                        serialized_definition_manual[field] = list(getattr(suggested_definition, field))
                    else:
                        serialized_definition_manual[field] = getattr(suggested_definition, field)

            # print("suggested_definition.synonyms[0]: ", suggested_definition.synonyms[0])
            for field in Definition._meta.fields:
                field_name = field.get_attname()
                print(field, ": ", getattr(suggested_definition,field_name))
            definition_model_field_names = [f.get_attname() for f in Definition._meta.fields]
            definitions_list = [definition for definition in definitions if definition.id != suggested_definition.id]
            selected_options, answer_options_list = get_field_data(word)
            word_model_field_names = [f.get_attname() for f in Word._meta.fields]
            # print("word_model_field_names: ", word_model_field_names)
            print("suggested_definition_data: ", json.loads(suggested_definition_data), " type: ", type(json.loads(suggested_definition_data)))
            # print("suggested_definition_data[0]: ", suggested_definition_data[0], " type: ", type(suggested_definition_data[0]))
            print("word_serialized: ", word_serialized)
            print("definitions_serialized: ", definitions_serialized)

            synonym_question, answer_options_list = format_synonym_question(word, suggested_definition, selected_options)
            synonym_questions.append({ "word_serialized": word_serialized, "synonym_question": model_to_dict(synonym_question), "answer_options_list": answer_options_list })

        print("*******synonym_questions: ", synonym_questions)
        context = {
            "synonym_questions": synonym_questions,
            "words": word_qs.values(),
            "word_serialized": word_serialized,
            "word_model_field_names": word_model_field_names,
            # "word_data": word_data,
            "definitions": definitions.values(),
            "definitions_serialized": definitions_serialized,
            "serialized_definition_manual": serialized_definition_manual,
            "definitions_data": definitions_data,
            "suggested_definition": suggested_definition,
            "suggested_definition_data": json.loads(suggested_definition_data),
            "selected_options": selected_options,
            "answer_options_list": answer_options_list,
            "synonym_question": model_to_dict(synonym_question),
            "synonym_questions": synonym_questions
        }
        return render(request, "question_maker/synonym_question.html", context)
    return render(request, "question_maker/synonym_question.html")

def format_synonym_question(word, suggested_definition, selected_options):
    print("suggested_definition: ", suggested_definition, " type: ", type(suggested_definition))
    print("word: ", word, " type: ", type(word))
    new_synonym = Synonym()
    new_synonym.word = word
    new_synonym.definition = suggested_definition
    new_synonym.save()

    synonyms_answer_options_list = []

    synonym_answer_word_value = random.choice(suggested_definition.synonyms)

    new_answer_option = SynonymAnswerOption()
    new_answer_option.synonym = new_synonym
    new_answer_option.is_correct = True
    new_answer_option.answer_type = "synonym"
    new_answer_option.value = synonym_answer_word_value
    new_answer_option.save()
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
        print("new_answer_option: }}}}}}++++ ", new_answer_option)
        new_answer_option.definition = random_def
        # setattr(synonym_answer_word, "definition", random_def)
        new_answer_option.save()

    new_answer_option.save()
    synonyms_answer_options_list.append(model_to_dict(new_answer_option))

    print("len(synonyms_answer_options_list): ", len(synonyms_answer_options_list))
    definition_model_field_names = [f.get_attname() for f in Definition._meta.fields]
    for field in definition_model_field_names:
        print("len(synonyms_answer_options_list): ", len(synonyms_answer_options_list))
        if len(synonyms_answer_options_list) < 5:
            if isinstance(getattr(suggested_definition, field), list) and field != "synonyms" and field != "examples":
                new_answer_option = SynonymAnswerOption()
                new_answer_option.synonym = new_synonym
                new_answer_option.is_correct = False
                new_answer_option.answer_type = field
                new_answer_option.value = random.choice(getattr(suggested_definition, field))
                new_answer_option.save()
                synonyms_answer_options_list.append(model_to_dict(new_answer_option))
        else:
            break
    print("BEFORE WHILE len(synonyms_answer_options_list): ", len(synonyms_answer_options_list))
    while len(synonyms_answer_options_list) < 5:
        for answer_option in selected_options:
            if len(synonyms_answer_options_list) < 5:
                new_answer_option = SynonymAnswerOption()
                new_answer_option.synonym = new_synonym
                for key, value in answer_option.items():
                    if key == "synonym":
                        new_answer_option.is_correct = True
                        new_answer_option.answer_type = "synonym"
                    else:
                        new_answer_option.is_correct = False
                        new_answer_option.answer_type = key
                    new_answer_option.value = value
                new_answer_option.save()
                synonyms_answer_options_list.append(model_to_dict(new_answer_option))
            else:
                break
    # print("GET_FIELDS: ", synonyms_answer_options_list[0].get_fields())
    return (new_synonym, synonyms_answer_options_list)


def synonyms_questions(request):
#    print(Word.objects.exclude(theme_relations = '')[0].theme_relations)
    if request.method == 'POST':

        random_words = create_synonyms.get_random_word(1)
        words_list = []
        index_counter = 1
        for random_word in random_words:
            word_data = process_word(random_word)
            words_list.append(word_data)
            index_counter += 1
#        synonym_question_data = create_synonym_question()
#        print("synonym_question_data: ", synonym_question_data)
#        context = synonym_question_data

            new_synonym = Synonym()
            new_synonym.word = random_word
            new_synonym.definition = word_data["suggested_definition"]
            new_synonym.save()

            synonyms_answer_options_list = []

            for answer_option in word_data["selected_options"]:
                new_answer_option = SynonymAnswerOption()
                new_answer_option.synonym = new_synonym
                for key, value in answer_option.items():
                    if key == "synonym":
                        new_answer_option.is_correct = True
                        new_answer_option.answer_type = "synonym"
                    else:
                        new_answer_option.is_correct = False
                        new_answer_option.answer_type = key
                    new_answer_option.value = value
                new_answer_option.save()
                synonyms_answer_options_list.append(new_answer_option)
        print("GET_FIELDS: ", synonyms_answer_options_list[0].get_fields())
        context = { "words_list":words_list, "synonym_id": new_synonym.id, "synonyms_answer_options_list": synonyms_answer_options_list}
        print("context: ", context)
        return render(request, "question_maker/synonyms_questions.html", context)
    return render(request, "question_maker/synonyms_questions.html")

def process_word(random_word):
    answer_options_list = []
    selected_options = []

    #        word_model_field_names = [f.name for f in Word._meta.get_fields()] #This gets Word fields and all related fields (by Foreign Key)

    selected_options, answer_options_list = get_field_data(random_word)
    print("answer_options_list[0]: ", answer_options_list[0]["similar_spellings"])
    print("type(answer_options_list[0].similar_spellings): ", type(answer_options_list[0]["similar_spellings"]), " ", answer_options_list[0]["similar_spellings"])

    while len(selected_options) < 4:
        selected_options.append({ "random_word": create_synonyms.get_random_word(1)[0].word })

    definitions = Definition.objects.filter(word=random_word)
    suggested_definition = random.choice(definitions)
    suggested_definition_dict = {}

    for field in suggested_definition.get_fields():
        list_form = field[1].replace('\'', '').replace("\"", "").replace("[", "").replace("]", "").split(",")
        if list_form[0] == 'None':
            suggested_definition_dict[field[0]] = None
        else:
            suggested_definition_dict[field[0]] = list_form

    if suggested_definition.synonyms is not '':
        synonyms_list = json.loads(getattr(suggested_definition, "synonyms").replace('\'', '\"'))
        selected_options.append({ "synonym": synonyms_list[random.randint(0,len(synonyms_list)-1)] })
    else:
        synonyms_list = []
    if suggested_definition.antonyms is not None:
        antonyms_list = json.loads(getattr(suggested_definition, "antonyms").replace('\'', '\"'))
        selected_options.append({ "antonym": antonyms_list[random.randint(0,len(antonyms_list)-1)] })
    else:
        antonyms_list = []
    definition_model_field_names = [f.get_attname() for f in Definition._meta.fields]
    definitions_list = [definition for definition in definitions if definition.id != suggested_definition.id]

    alternate_definitions_list = []
    for definition in definitions_list:
        alternate_definitions_dict = {}
        for field in definition.get_fields():
            list_form = field[1].replace('\'', '').replace("\"", "").replace("[", "").replace("]", "").split(",")
            if list_form[0] == 'None':
                alternate_definitions_dict[field[0]] = None
            else:
                alternate_definitions_dict[field[0]] = list_form
        alternate_definitions_list.append(alternate_definitions_dict)


    print("suggested_definition_dict: ", suggested_definition_dict)
    return {"word": random_word, "suggested_definition": suggested_definition, "suggested_definition_dict": suggested_definition_dict, "alternate_definitions": definitions_list, "alternate_definitions_list": alternate_definitions_list, "synonyms_list": synonyms_list, "antonyms_list": antonyms_list, "answer_options_list": answer_options_list, "selected_options": selected_options }

def get_field_data(random_word):
    word_model_field_names = [f.get_attname() for f in Word._meta.fields] #This gets only Word fields
    selected_options_list = []
    answer_options = []
    for field in word_model_field_names:
        if field != "word" and field != "id" and getattr(random_word, field) != None:
            field_data_list = getattr(random_word, field)
            if len(field_data_list) > 1:
                selected_options_list.append({ field: field_data_list[random.randint(0,len(field_data_list)-1)] })
            elif len(field_data_list) == 1:
                selected_options_list.append({ field: field_data_list[0] })
            answer_options.append({ field: field_data_list })
        else:
            continue
    return (selected_options_list, answer_options)

def analogies_questions(request):
    return render(request, "question_maker/analogies_questions.html")

def create_synonym_question():
    synonym_data = create_synonyms.create_synonym()

    new_word = Word()
    word = synonym_data['question_word']
    word.similar_spellings = synonym_data.similar_spellings
    word.similar_sound = synonym_data.similar_sound
    word.similar_relations = synonym_data.similar_relations
    word.associations = synonym_data.associations
    word.save()

    new_synonym = Synonym()
    new_synonym.word = word
    new_synonym.save()

    synonym_answer_list = []

    word_model_field_names = [f.name for f in MyModel._meta.get_fields()]

    for field_name in word_model_field_names:
        new_synonym_answer = SynonymAnswer()
        new_synonym_answer.synonym = new_synonym
        if field_name == "word":
            new_synonym_answer.is_correct = True
            new_synonym_answer.value = synonym_data.synonym
        else:
            new_synonym_answer.is_correct = False
            new_synonym_answer.value = synonym_data.field_name
        new_synonym_answer.save()
        synonym_answer_list.append(new_synonym_answer)


        new_synonym_answer.synonym = new_synonym

    for result in synonym_data.results:
#         if option.type == "synonym":
#            new_word.similar_spellings = synonym_data.alternate_words
#         elif option.type == "antonym":
#            new_word.similar_sounds = synonym_data.alternate_words
#         elif option.type == "similar":
#            new_word.theme_relations = synonym_data.alternate_words
#         elif option.type == "theme":
#            new_word.associations = synonym_data.alternate_words
#         else:
#            new_word.similar_spellings = synonym_data

        new_definition = Definition()
        new_definition.word = word
        new_definition.definition_text = result.definition
        new_definition.save()

        if forloop.counter0 == synonym_data.definition_index:
            new_synonym.definition = new_definition
            new_synonym.save()

        for key, value in  result.items():
            if key == "partOfSpeech":
                new_definition.part_of_speech = result.partOfSpeech
            elif key == "synonyms":
                new_definition.synonyms_list = result.synonyms
            elif key == "antonyms":
                new_definition.antnonyms_list = result.antonyms
            elif key == "entails":
                new_definition.entails_list = result.entails
            elif key == "also":
                new_definition.also_list = result.also
            elif key == "attribute":
                new_definition.attribute_list = result.attribute
            elif key == "similarTo":
                new_definition.similar_to_list = result.similarTo
            elif key == "typeOf":
                new_definition.type_of_list = result.typeOf
            elif key == "hasTypes":
                new_definition.has_types_list = result.hasTypes
            elif key == "partOf":
                new_definition.part_of_list = result.partOf
            elif key == "hasParts":
                new_definition.has_parts_list = result.hasParts
            elif key == "instanceOf":
                new_definition.is_instance_of_list = result.instanceOf
            elif key == "hasInstances":
                new_definition.has_instances_list = result.hasInstances
            elif key == "memberOf":
                new_definition.member_of_list = result.memberOf
            elif key == "hasMembers":
                new_definition.has_members_list = result.hasMembers
            elif key == "substanceOf":
                new_definition.substance_of_list = result.substanceOf
            elif key == "hasSubstances":
                new_definition.has_substances_list = result.hasSubstances
            elif key == "inCategory":
                new_definition.in_category_list = result.inCategory
            elif key == "hasCategories":
                new_definition.has_categories_list = result.hasCategories
            elif key == "usageOf":
                new_definition.usage_of_list = result.usageOf
            elif key == "hasUsages":
                new_definition.has_usages_list = result.hasUsages
            elif key == "inRegion":
                new_definition.in_region_list = result.inRegion
            elif key == "regionOf":
                new_definition.region_of_list = result.regionOf
            elif key == "pertainsTo":
                new_definition.pertains_to_list = result.pertainsTo
            elif key == "examples":
                new_definition.examples_list = result.examples
        new_definition.save()

    return { "synonym": new_synonym, "synonym_options": synonym_answer_list }
