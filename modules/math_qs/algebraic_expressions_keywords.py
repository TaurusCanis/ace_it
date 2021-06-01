import random
def q_1():
    names = ["Tom", "Lindsay"]
    items = ["marbles", "sticks"]
    vars = ["x", "y", "z"]
    situation = ["more", "fewer"]
    name_1 = random.choice(names)
    name_2 = random.choice(names)
    while name_2 == name_1:
        name_2 = random.choice(names)
    item = random.choice(items)
    var_name = random.choice(vars)
    more_or_fewer = random.choice(situation)
    num_of_name_2_var = random.randint(3,8)
    question_text = f"<p>{name_1}&nbsp;has <strong><em>{var_name}</em></strong><em>&nbsp;</em>{more_or_fewer} {item} &nbsp;than {name_2}. {name_2} has {num_of_name_2_var} {item}. How many {item} does {name_1}&nbsp;have, in terms of <strong><em>{var_name}</em></strong>?&nbsp;</p>\n"
    print(question_text)
    if more_or_fewer == "more":
        answer = f"{num_of_name_2_var} + {var_name}"
        options = [
            {
                "option": answer,
                "correct": True
            },
            {
                "option": f"\\(\\frac{{k}}{num_of_name_2_var}\\)",
                "correct": False
            },
            {
                "option": f"\\(\\frac{num_of_name_2_var}{{k}}\\)",
                "correct": False
            },
            {
                "option": f"<em>k&nbsp;</em>- {num_of_name_2_var}",
                "correct": False
            },
            {
                "option": f"{num_of_name_2_var} -&nbsp;<em>k</em>",
                "correct": False
            }
        ]
    else:
        answer = f"{num_of_name_2_var} - {var_name}"
        options = [
            {
                "option": answer,
                "correct": True
            },
            {
                "option": f"\\(\\frac{{k}}{num_of_name_2_var}\\)",
                "correct": False
            },
            {
                "option": f"\\(\\frac{num_of_name_2_var}{{k}}\\)",
                "correct": False
            },
            {
                "option": f"<em>k&nbsp;</em>- {num_of_name_2_var}",
                "correct": False
            },
            {
                "option": f"{num_of_name_2_var} +&nbsp;<em>k</em>",
                "correct": False
            }
        ]
    # Need to include this in above dicts
    # distractor_rationale = [
    # "You may have taken the unknown score to be given as a fraction of Anna's score, but the term \"fewer\" indicates that the difference is based on subtraction.",
    # "You may have taken the unknown score to be given as a ratio of Anna's score to the difference, but the term \"fewer\" indicates that the difference is based on subtraction.",
    # "You identified a score that is 7 points fewer than <em>k&nbsp;</em>points, but the expression must represent&nbsp;<em>k&nbsp;</em>points fewer than 7.",
    # "The number of points Franz scored is the difference between 7 and&nbsp;<em>k</em>, since Franz scored&nbsp;<em>k&nbsp;</em>fewer points&nbsp;fewer.",
    # "You identified a score representing&nbsp;<em>k&nbsp;</em>points more that Anna's score, rather than&nbsp;<em>k&nbsp;</em>points fewer."
    # ]

    random.shuffle(options)

    return { "question_text": question_text, "options": options }
