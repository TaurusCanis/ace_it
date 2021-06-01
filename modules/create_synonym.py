import json, random, requests
from question_maker.models import *
from random import choice, sample

def get_random_word(n):
    pks = Word.objects.values_list('pk', flat=True)
    random_pks = sample(list(pks), n)
    has_synonym = False
    while not has_synonym:
        random_words = Word.objects.filter(pk__in=random_pks).exclude(definition__synonyms=None)
        print("random_words.count(): ", random_words.count())
        if random_words.count() > 0:
            has_synonym = True
        else:
            random_pks = sample(list(pks), n)
        print("has_synonym: ", has_synonym)
    # for word in random_words:
    #     definition = get_definitions(word.id)
    #     suggested_definition = random.choice(definitions.exclude(synonyms=None))
    return random_words

def get_definitions(pk):
    return Definition.objects.filter(word_id=pk)

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

def get_dictionary_data(word):
    print("word: ", word)
    #How to handle if word is not in dictionary?
    url = "https://wordsapiv1.p.rapidapi.com/words/" + word

    headers = {
        'x-rapidapi-key': "5d633d11f3mshee22825861d1068p13d37cjsnc0266c59c324",
        'x-rapidapi-host': "wordsapiv1.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers)
    response_json = json.loads(response.text)
    print(response_json)
    if "results" in response_json:
        return response_json["results"]
    else:
        return "No Definition"
