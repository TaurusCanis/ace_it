import random

solve_for = random.choice(["leg", "hypotenuse"])

if solve_for == "leg":
    leg_length = random.randint(3,9)
    hypotenuse = f"\\(str({leg_length}) + \\sqrt{2}\\)"
    question = f"<p>An isosceles right triangle has a hypotenuse of length {hypotenuse}. What is the length of the leg of this triangle?</p>\n"
    answer = leg_length

    options = [
        {
        "option":answer,
        "correct":True
        },
        {
        "option":hypotenuse,
        "correct":False
        },
        {
        "option":"\\(\\sqrt{2}\\)",
        "correct":False
        },
        {
        "option":f"\\(2\\times{leg_length}\\)",
        "correct":False
        },
        {
        "option":f"\\(2\\times{leg_length}\\\\sqrt{2}\\)",
        "correct":False
        }
    ]

else:
    leg_length = random.randint(3,9)
    question = f"<p>An isosceles right triangle has a leg of length {leg_length}. What is the length of the hypotenuse of this triangle?</p>\n"
    answer = f"\\(str({leg_length}) + \\sqrt{2}\\)"

    options = [
        {
        "option":answer,
        "correct":True
        },
        {
        "option":leg_length,
        "correct":False
        },
        {
        "option":"\\(\\sqrt{2}\\)",
        "correct":False
        },
        {
        "option":f"\\(2\\times{leg_length}\\)",
        "correct":False
        },
        {
        "option":f"\\(2\\times{leg_length}\\\\sqrt{2}\\)",
        "correct":False
        }
    ]

#     "distractor_rationale_response_level":[
# "You may have confused the hypotenuse with another side with the same length as the leg described.",
# "You may have taken the hypotenuse length to be the sum of the two leg lengths, but&nbsp;the length of a hypotenuse is the square root of the sum of the squares of the two leg lengths.",
# "You may have taken the hypotenuse length to be the square root of the given length, but&nbsp;the length of a hypotenuse is the square root of the sum of the squares of the two leg lengths.",
# "The length of the hypotenuse&nbsp; is the square root of the sum of the squares of the two leg lengths. The length of this triangle is the square root of 8, the sum of 4 and 4, since each leg has a length of 2. Since the square root of 4 can be factored out of the square root o 8, the hypotenuse length is equivalent to \\(2\\sqrt{2}\\),",
# "You did factored 4 instead of the square root of 4 out of the square root of 8."
# ]

random.shuffle(options)
print(question)
letter_index = 65
for option in options:
    print(chr(letter_index) + ": " + str(option["option"]))
    letter_index += 1

user_response = input("Choose an answer option: ")
if options[ord(user_response.upper()[0]) - 65]["correct"]:
    print("CORRECT!")
else:
    print("INCORRECT!")
