import json

with open("SSAT2000_full_dictionary_2.json") as file:
    data = json.load(file)
    
#print(data)

#find_word = "etch"
#
count = 1
for word in data:
    print(str(count) + ": ", json.loads(word)["word"])
    count += 1
#    try:
#        if json.loads(word)["word"] == find_word:
#            print(word)
#            break
#    except:
#        pass

