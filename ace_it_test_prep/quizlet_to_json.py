import json

with open("TestInnovatorsQuizlet300.txt", "r") as txt:
    line_count = 1
    terms = []
    for line in txt.readlines():

        if line_count % 4 == 1:
            if ";" in line:
                reformatted_line = line.replace("; ", ", ")
                split_line = reformatted_line.split(";")
                example = split_line[0]
                new_term_dict["example"] = example
                terms.append(new_term_dict)
                new_term_dict = {}
                next_term = split_line[1]
            else:
                if "-" in line:
                    next_term = line
                else:
                    new_term_dict["example"] = line.rstrip("\n")
                    terms.append(new_term_dict)


            next_term_split = next_term.split("-")

            try:
                new_term_dict = {}
                next_term_term = next_term_split[0]
                next_term_part_of_speech = next_term_split[1]
                new_term_dict["word"] = next_term_term
                new_term_dict["part_of_speech"] = next_term_part_of_speech.rstrip("\n")
            except:
                pass

        elif line_count % 4 == 3:
            stripped_line = line.rstrip("\n")
            synonyms = stripped_line.split(",")
            new_term_dict["synonyms"] = synonyms
            print("new_term_dict: ", new_term_dict)

        line_count += 1
    print("terms: ", type(terms))
    terms_json = json.dumps(terms)
    print("terms_json: ", type(terms_json))

    # with open('TestInnovatorsQuizlet300.json', 'w') as f:
    #     json.dump(terms, f)
