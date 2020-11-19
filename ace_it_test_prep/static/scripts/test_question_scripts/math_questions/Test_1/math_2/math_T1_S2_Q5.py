import random

diameter_or_radius = random.choice(["diameter", "radius"])

measurement = random.randrange(18,50,2)

question = f"<p>The {diameter_or_radius} of a circle is {measurement} inches. What is the circumference, in inches, of the circle?</p>\n"

if diameter_or_radius == "diameter":
    answer = str(measurement) + "\\(\\pi\\)"

    options = [
        {
        "option": answer,
        "correct": True
        },
        {
        "option": str(measurement / 4) + "\\(\\pi\\)",
        "correct": False
        },
        {
        "option": str(measurement / 2) + "\\(\\pi\\)",
        "correct": False
        },
        {
        "option": str(((measurement / 2) ** 2)/2) + "\\(\\pi\\)",
        "correct": False
        },
        {
        "option": str((measurement / 2) ** 2) + "\\(\\pi\\)",
        "correct": False
        }
    ]
else:
    answer = str(measurement * 2) + "\\(\\pi\\)"

    options = [
        {
        "option": answer,
        "correct": True
        },
        {
        "option": str(measurement / 2) + "\\(\\pi\\)",
        "correct": False
        },
        {
        "option": str(measurement) + "\\(\\pi\\)",
        "correct": False
        },
        {
        "option": str(measurement ** 2) + "\\(\\pi\\)",
        "correct": False
        },
        {
        "option": str((measurement / 2) ** 2) + "\\(\\pi\\)",
        "correct": False
        }
    ]


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
    print(answer)

# "distractor_rationale_response_level":[
# "You make have taken the circumference of a circle to be the product of&nbsp;π and the half the radius, rather than the product of&nbsp;π and twice the radius.",
# "You took the circumference of a circle to be the product of&nbsp;π and the radius, rather than the product of&nbsp;π and the diameter.",
# "The circumference of a circle is the product of the diameter and&nbsp;π. So, the circumference in inches of a circle with a diameter of 24 inches is 24π.",
# "You applied the circle and triangle area formulas, multiplying&nbsp;π by the square of the radius instead of the diameter, and then halving the result.",
# "You applied the area formula, multiplying&nbsp;π by the square of the radius instead of the diameter."
# ]
