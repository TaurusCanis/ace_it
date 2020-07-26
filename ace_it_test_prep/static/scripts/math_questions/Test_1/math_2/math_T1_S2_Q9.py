import random

trap_mass = random.randint(125,175)
mouse_mass = random.randint(3,6)

answer = trap_mass - (mouse_mass * 28) - 1

question = f"<p>The mass required to set off a mouse trap is {trap_mass} grams. Of the following, what is the largest mass of cheese, in grams, that a {mouse_mass}-ounce mouse could carry and <u>not</u> set off the trap? (1 ounce = 28 grams)</p>\n"

options = [
    {
    "option": answer,
    "correct": True
    },
    {
    "option": answer + 1,
    "correct": False
    },
    {
    "option": "28",
    "correct": False
    },
    {
    "option": mouse_mass * 28,
    "correct": False
    },
    {
    "option": trap_mass - (mouse_mass * 25),
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
# "You used the conversion rate as the maximum mass of cheese, but the conversion rate is only used to determine the mass of the mouse in grams.",
# "A mouse weighing 4 ounces has a mass of 112 grams, since 4&nbsp;× 28 = 112. Since 157&nbsp;– 112 = 45, the cheese must weigh less than 45 grams for the trap to not be be set off. The largest given mass that is less than 45 grams is 44 grams.",
# "You solved the equation 157&nbsp;–&nbsp;<em>x&nbsp;</em>= 112, but overlooked that the solution represents the minimum mass of cheese that would set off the trap.",
# "You may have multiplied 4 by 25 instead of 28 to find the mass of the mouse in grams, but that mass is 128 grams.",
# "You identified the mass of the mouse in grams, rather than the maximum mass of the cheese that will not set off the trap."
# ]
