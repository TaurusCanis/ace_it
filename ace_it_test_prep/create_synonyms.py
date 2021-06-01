import json, random, requests

with open("SSAT2000_full_dictionary_2.json") as file:
    data = json.load(file)
    
question_word = json.loads(data[random.randint(0,len(data))])

print("WORD_DATA: ", question_word)
#print("WORD: ", question_word["word"])


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

print("RESPONSE 1: ", response_1)


url = "https://twinword-word-associations-v1.p.rapidapi.com/associations/"

querystring = {"entry":question_word["word"]}

headers = {
    'x-rapidapi-key': "5d633d11f3mshee22825861d1068p13d37cjsnc0266c59c324",
    'x-rapidapi-host': "twinword-word-associations-v1.p.rapidapi.com"
    }

response_2 = json.loads(requests.request("GET", url, headers=headers, params=querystring).text)["associations_array"]

print("RESPONSE 2: ", response_2)

print("*************")
print("1. ", question_word["word"])
if len(synonyms) > 0:
    print("A. ", synonyms[random.randint(0,len(synonyms)-1)])
else:
    print("A. ", json.loads(data[random.randint(0,len(data)-1)])["word"])
if len(antonyms) > 0:
    print("B. ", antonyms[random.randint(0,len(antonyms)-1)])
else:
    print("B. ", json.loads(data[random.randint(0,len(data)-1)])["word"])
if len(response_1) > 0:
    print("C. ", response_1[random.randint(0,len(response_1)-1)])
else:
    print("C. ", json.loads(data[random.randint(0,len(data)-1)])["word"])
if len(response_2) > 0:
    print("D. ", response_2[random.randint(0,len(response_2)-1)])
else:
    print("D. ", json.loads(data[random.randint(0,len(data)-1)])["word"])
print("E. ", json.loads(data[random.randint(0,len(data)-1)])["word"])

