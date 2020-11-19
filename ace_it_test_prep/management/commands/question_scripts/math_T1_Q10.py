import random

items = ["staple", "paperclip"]
item = random.choice(items)

weight = random.randint(11,49)
num_items = random.choice([50, 100, 200, 250, 500])

question = f"<p>One {item} weighs {weight} milligrams. If a box of {item}s holds {num_items} {item}s, how many <u>grams</u> of {item}s does the box hold?</p>\n"

answer = weight * num_items / 1000

options = [
    {
    "option":answer,
    "correct": True
    },
    {
    "option":weight * num_items / 100,
    "correct": False
    },
    {
    "option":weight * num_items ,
    "correct":False
    },
    {
    "option":abs(answer - 1),
    "correct":False
    },
    {
    "option":abs((weight * num_items / 100) - 10),
    "correct":False
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
"You may have made an error in calculation when multiplying 250 by 31 or 0.0031 and not carried 1 to the next column when multiplying 3 by 5.",
"Since a milligram is&nbsp;\\(\\frac{1}{1,000}\\) of a gram, 31 milligram is equal to 0.0031 grams (the result of dividing 31 by 1,000. The product 750 and 0.0031 is 7.75.",
"You may have made an error in calculation when multiplying 250 by 31 or 0.0031 and not carried 1 to the next column when multiplying 3 by 5, and you may have also divided by 100 instead of 1,000 when converting milligrams to grams.",
"You divided by 100 instead of 1,000 when converting milligrams to grams.",
"You calculated the number of milligrams of staples in a box, rather than the number of grams."
]
