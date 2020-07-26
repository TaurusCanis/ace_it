import random

num = random.randint(25,75)

question = f"<p>If {num} × <em>a</em><em>&nbsp;</em>= {num}, then what is the value of {num} − <em>a&nbsp;</em>?</p>\n"

answer = num - 1

options = [
    {
    "option": answer,
    "correct": True
    },
    {
    "option":f"\\(\\frac{1}{{{num}}}\\)",
    "correct": False
    },
    {
    "option":"1",
    "correct": False
    },
    {
    "option": 0,
    "correct": False
    },
    {
    "option": num + 1,
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
# "You used 50&nbsp;instead of 1 for the value of&nbsp;<em>a</em>.",
# "You identified the value of&nbsp;<em>a&nbsp;</em>divided by 50&nbsp;rather than&nbsp; 50 − <em>a</em>.",
# "You identified the value of&nbsp;<em>a</em>&nbsp;rather than the value of&nbsp;50 − <em>a</em>.",
# "If 50&nbsp;×&nbsp;<em>a&nbsp;</em>= 50, then&nbsp;<em>a&nbsp;</em>= 1, for the product of any number (other than zero) and 1 is that number. So,&nbsp; 50 − <em>a&nbsp;</em>=&nbsp; 50 − 1.",
# "You added the value of&nbsp;<em>a</em>&nbsp;to 50 instead of subtracting."
# ]
