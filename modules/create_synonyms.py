import json, random, requests
from question_maker.models import *
from random import choice, sample

def get_random_word(n):
    pks = Word.objects.values_list('pk', flat=True)
    random_pks = sample(list(pks), n)
    random_words = Word.objects.filter(pk__in=random_pks)
    return random_words

def create_synonym():
    with open("ace_it_test_prep/SSAT2000_full_dictionary_2.json") as file:
        data = json.load(file)
        
    question_word = json.loads(data[random.randint(0,len(data)-1)])
    definition_index = random.randint(0,len(question_word["results"])-1)

    print("WORD_DATA: ", question_word)
    print("DEFINTION INDEX: ", definition_index)
    #print("WORD: ", question_word["word"])
    
    definition = question_word["results"][definition_index]["definition"]

    print()

    synonyms = []
    antonyms = []
    entails = []
    definitions = []

    for result in question_word["results"]:
    #    print("RESULT: ", result)
        if "synonyms" in result:
            synonyms.extend(result["synonyms"])
        if "antonyms" in result:
            antonyms.extend(result["antonyms"])
        if "entails" in result:
            entails.extend(result["entails"])
        definitions.append(result["definition"])

    #synonyms = question_word["results"][0]["synonyms"]
    #definition = question_word["results"][0]["definition"]

    print("SYNONYMS: ", synonyms)
    print("ANTONYMS: ", antonyms)
    print("ENTAILS: ", entails)
    print("DEFINTIONS: ", definitions)

    #get close/themtic words
    url = "https://twinword-word-graph-dictionary.p.rapidapi.com/theme/"

    querystring = {"entry":question_word["word"]}

    headers = {
        'x-rapidapi-key': "5d633d11f3mshee22825861d1068p13d37cjsnc0266c59c324",
        'x-rapidapi-host': "twinword-word-graph-dictionary.p.rapidapi.com"
        }

    response_1 = json.loads(requests.request("GET", url, headers=headers, params=querystring).text)["theme"]
#    response_1 = []
#
#    print("RESPONSE 1: ", response_1)


    url = "https://twinword-word-associations-v1.p.rapidapi.com/associations/"

    querystring = {"entry":question_word["word"]}

    headers = {
        'x-rapidapi-key': "5d633d11f3mshee22825861d1068p13d37cjsnc0266c59c324",
        'x-rapidapi-host': "twinword-word-associations-v1.p.rapidapi.com"
        }

    response_2 = json.loads(requests.request("GET", url, headers=headers, params=querystring).text)["associations_array"]
#    response_2 = []
#
#    print("RESPONSE 2: ", response_2)

    # similar spelling
    url_sp = 'https://api.datamuse.com/words?sp=' + question_word["word"]
    similar_spelling = [value['word'] for value in json.loads(requests.request("GET", url_sp).text)]
    
    #similar sound
    url_sl = 'https://api.datamuse.com/words?sl=' + question_word["word"]
    similar_sound = [value['word'] for value in json.loads(requests.request("GET", url_sl).text)]
    
    print("SIMILAR SPELLING: ", similar_spelling)
    print("SIMILAR SOUND: ", similar_sound)

    print("*************")
    print("1. ", question_word["word"])
    if len(synonyms) > 0:
        synonym = synonyms[random.randint(0,len(synonyms)-1)]
        print("A. ", synonym)
    else:
        synonym = json.loads(data[random.randint(0,len(data)-1)])["word"]
        print("A. ", synonym)
    if len(antonyms) > 0:
        antonym = antonyms[random.randint(0,len(antonyms)-1)]
        print("B. ", antonym)
    else:
        antonym = json.loads(data[random.randint(0,len(data)-1)])["word"]
        print("B. ", antonym)
    if len(response_1) > 0:
        similar = response_1[random.randint(0,len(response_1)-1)]
        print("C. ", similar)
    else:
        similar = json.loads(data[random.randint(0,len(data)-1)])["word"]
        print("C. ", similar)
    if len(response_2) > 0:
        theme = response_2[random.randint(0,len(response_2)-1)]
        print("D. ", theme)
    else:
        theme = json.loads(data[random.randint(0,len(data)-1)])["word"]
        print("D. ", theme)
    alternate = json.loads(data[random.randint(0,len(data)-1)])["word"]
    print("E. ", alternate)

    return {
        "question_word": question_word["word"],
        "definition_index": definition_index,
        "definition": definition,
        "synonym": synonym,
        "similar_spelling": similar_spelling,
        "similar_sound": similar_sound,
        "theme_relations": theme,
        "associations": similar,
        "results": question_word["results"],
#        "options": [
#            {
#                "type": "synonym",
#                "selected_word": synonym,
#                "alternate_words": synonyms
#            },
#            {
#                "type": "antonym",
#                "selected_word": antonym,
#                "alternate_words": antonyms
#            },
#            {
#                "type": "similar",
#                "selected_word": similar,
#                "alternate_words": response_1
#            },
#            {
#                "type": "theme",
#                "selected_word": theme,
#                "alternate_words": response_2
#            },
#            {
#                "type": "alternate",
#                "selected_word": alternate
#            }
#        ]
    }

