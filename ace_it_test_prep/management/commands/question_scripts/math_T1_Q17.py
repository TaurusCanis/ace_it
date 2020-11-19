import random

num_1 = random.randint(1,12)
num_1_sign = random.choice(["+", "-"])
num_2 = random.randint(1,12)
num_2_sign = random.choice(["+", "-"])

question = f"<p>What are the solutions to the equation&nbsp;\\(\\left(x{num_1_sign}{num_1}\\right)\\left(x{num_2_sign}{num_2}\\right)=0\\)&nbsp;?</p>\n"

answer_1 = eval(f"-{num_1_sign}{num_1}")
answer_2 = eval(f"-{num_2_sign}{num_2}")
answer = f"\\(x={answer_1}\\)&nbsp;and&nbsp;\\(x={answer_2}\\)"

options = [
    {
    "option":answer,
    "correct":True
    },
    {
    "option":"\\(x=" + str(eval(f"{num_1_sign}{num_1}")) + "\\)&nbsp;and&nbsp;\\(x=" + str(eval(f"{num_2_sign}{num_2}")) + "\\)",
    "correct":False
    },
    {
    "option":"\\(x=" + str(eval(f"-{num_1_sign}{num_1}")) + "\\)&nbsp;and&nbsp;\\(x=" + str(eval(f"{num_2_sign}{num_2}")) + "\\)",
    "correct":False
    },
    {
    "option":"\\(x=" + str(eval(f"{num_2} - {num_1}")) + "\\)&nbsp;and&nbsp;\\(x=" + str(eval(f"-{num_2_sign}{num_2}")) + "\\)",
    "correct":False
    },
    {
    "option":"\\(x=" + str(eval(f"{num_2} - {num_1}")) + "\\)&nbsp;and&nbsp;\\(x=" + str(eval(f"-{num_1_sign}{num_1}")) + "\\)",
    "correct":False
    }
]


random.shuffle(options)
print(question)
print(num_1, " ", num_2 )
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
# "You may have taken the numbers added to the variables to represent the solutions, but the actual solutions are the values for&nbsp;<em>x</em>&nbsp;when&nbsp;<em>x&nbsp;</em>+ 5 = 0 and&nbsp;<em>x&nbsp;</em>– 1 = 0",
# "The product of&nbsp;<em>x&nbsp;</em>+ 5 and&nbsp;<em>x&nbsp;</em>–&nbsp;1 is 0 if either expression has a value of 0. So, the solutions of the equation are the solutions of&nbsp;<em>x&nbsp;</em>+ 5 = 0 and&nbsp;<em>x&nbsp;</em>–&nbsp;1 = 0, which are –5 and 1, respectively.",
# "You identified the solution of&nbsp;<em>x&nbsp;</em>–&nbsp;5 = 0 instead of&nbsp;<em>x&nbsp;</em>+ 5 = 0.",
# "You subtracted 1 from 5 instead of solving&nbsp;<em>&nbsp;x</em>&nbsp;– 1 = 0.",
# "You subtracted 1 from 5 instead of solving&nbsp;<em>&nbsp;x</em>&nbsp;+ 5 = 0."
# ]
