import json
import requests
import time, threading

headers = {
    'x-rapidapi-host': "wordsapiv1.p.rapidapi.com",
    'x-rapidapi-key': "5d633d11f3mshee22825861d1068p13d37cjsnc0266c59c324"
    }

with open("SSAT3000.json") as f:
    data_json = json.load(f)

index = 500
data_list = []

def get_word(word, index):
    while index < 1000:
        time.sleep(-time.time()%1)
        url = "https://wordsapiv1.p.rapidapi.com/words/" + data_json[index]
        response = requests.request("GET", url, headers=headers)
        data_list.append(response.text)
        index += 1

    # threading.Timer(2, get_word(data_json[index], index)).start()

get_word(data_json[index], index)

# for item in data_list:
#     print("item: ", item)

with open('SSAT2000_full_dictionary_2.json', 'w') as f:
    json.dump(data_list, f)
