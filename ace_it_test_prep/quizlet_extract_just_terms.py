import json

with open("SSAT2000.txt", "r") as txt:
    line_count = 1
    terms = []
    for line in txt.readlines():
        if "::" in line:
            split_line = line.split("::")
            if split_line[0] != "\n":
                terms.append(split_line[0].lower())
    print("terms: ", terms)
    with open('SSAT3000.json', 'w') as f:
        json.dump(terms, f)
