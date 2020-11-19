import random

names = ["Mr. Williams", "Ms. Smith"]
name = random.choice(names)

items = ["parking lot", "card collection"]
item = random.choice(items)

first_percent_change = random.randrange(15,35,5)
second_percent_change = random.randrange(10,30,10)

question = f"<p>{name} sold {first_percent_change}% of their {item} to their neighbor. Later that year they sold {second_percent_change}% of the remainder of his {item} to another neighbor. What percent of the original {item} do they still own?</p>\n"

answer = ((100 - second_percent_change) / 100) * (100 - first_percent_change)

options = [
    {
    "option": answer,
    "correct": True
    },
    {
    "option": str(eval(f"100 - {answer}")) + "%",
    "correct": False
    },
    {
    "option": str(eval(f"{first_percent_change} + {second_percent_change}")) + "%",
    "correct": False
    },
    {
    "option": str(eval(f"100 - {first_percent_change} - {second_percent_change}")) + "%",
    "correct": False
    },
    {
    "option": str(eval(f"100 - {first_percent_change}")) + "%",
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


# "distractor_rationale_response_level":[
# "You took 20% off of 20%, but the amount of area remaining is 80% of 80%.",
# "You added 20% to 20%,&nbsp;but the amount of area remaining is 80% of 80%.",
# "You subtracted 20% from 80% instead of taking off 20% of 80%.",
# "After the first sale, he had 80% of the lot area remaining. After selling of 20% of the remaining area, he still had 80% of the 80%, and 80% of 80% is 64%.",
# "You calculated the percent remaining after the first sale."
# ]
