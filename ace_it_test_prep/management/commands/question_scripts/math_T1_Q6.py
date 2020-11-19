import random

# "stimulus":"<p><img class=\"lrn-image-center\" height=\"87\" src=\"https://dw6y82u65ww8h.cloudfront.net/organisations/75/351d17af-0ee2-4145-851a-c1a229488f4b.PNG\" width=\"80\" /></p>\n\n<p>If the perimeter of the square shown is 640, what is the value of&nbsp;\\(x\\)?</p>\n",


side_length = random.choice([4,8,10,12])
multiple = random.choice([5,10,20,25])
perimeter = side_length ** 2 * multiple

question = f"<p>If the perimeter of a square with side length of {side_length}&nbsp;\\(x\\) is {perimeter}. What is the value of &nbsp;\\(x\\)?</p>"

options = [
    {
        "option": (perimeter / 4) / side_length,
        "correct": True
    },
    {
        "option": perimeter / 8,
        "correct": False
    },
    {
        "option": (perimeter / 2) / side_length,
        "correct": False
    },
    {
        "option": perimeter / side_length,
        "correct": False
    },
    {
        "option": (perimeter / 4),
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

distractor_rationale = [
"You may have divided the perimeter by 8 instead 4 to get the length of a side.",
"The side length of a square is one quarter of the perimeter. Since 640&nbsp;÷ 4 = 160, the equation 160 = 8<em>x</em>&nbsp;can be used to find the value of&nbsp;<em>x.&nbsp;</em>The result of dividing 160 by 8 is 20.",
"You may have taken the length of a side of the square to be half of the perimeter rather than a fourth of the perimeter.",
"You may have divided the perimeter instead of a side length by 8.",
"You applied the perimeter formula and divided 640 by 4, but you may have take the result to be the value of&nbsp;<em>x&nbsp;</em>rather than 8<em>x</em>."
]
