import random
# NOT FINISHED!!!!
def hard():
    num_options = random.randint(3,10)
    num_objects = random.randrange(50, 350, 50)
    max_or_min = random.choice(["maximum", "minimum"])
    question_text = f"At a central train station, there are {num_options} different train routes with \
    trains that leave every 6 minutes, 10 minutes, 12 minutes, and 15 minutes. \
    If each train can hold up to {num_objects} passengers, what is the {max_or_min} number of passengers \
    who can leave the station on a train in one hour?"

    print(question_text)