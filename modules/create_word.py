import json, requests

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
