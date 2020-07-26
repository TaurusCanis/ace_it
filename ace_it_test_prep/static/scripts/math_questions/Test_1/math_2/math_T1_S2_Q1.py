import random

width = random.randint(8,16)
length = random.randint(8,16)

if length == width:
    length = random.randint(8,16)

area = width * length

question = f"<p>If the area of a rectangle is {area} square centimeters, and its length is {length} centimeters, what is the width of the rectangle?</p>\n"

answer = width

options = [
    {
    "option": answer,
    "correct": True
    },
    {
    "option": answer + random.choice([1,2]),
    "correct": False
    },
    {
    "option": answer - random.choice([1,2]),
    "correct": False
    },
    {
    "option": answer + random.choice([3,4]),
    "correct": False
    },
    {
    "option": answer - random.choice([3,4]),
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
# "You may have performed a calculation error when dividing the area by the length, as the product of 7 and 16 is 112.",
# "You may have performed a calculation error when dividing the area by the length, as the product of 8 and 16 is 128.",
# "The area of a rectangle is the product of the length and width. So, the width of a rectangle is the area divided by the length. Since 144&nbsp;÷ 16 = 9, the rectangle has a width of 9 centimeters.",
# "You may have performed a calculation error when dividing the area by the length, as the product of 10 and 16 is 160.",
# "You may have performed a calculation error when dividing the area by the length, as the product of 12 and 16 is 192."
# ]
