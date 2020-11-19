import random

num_1 = random.randint(11, 29)
num_2 = random.randint(15, 25)
while num_2 == num_1:
    num_2 = random.randint(15, 25)

sum = num_1 + num_2
difference = abs(num_2 - num_1)

smaller_or_larger = random.choice(["smaller", "larger"])

question = f"<p>Two numbers whose difference is {difference} add up to {sum}. What is the {smaller_or_larger} of these two numbers?</p>\n"

if smaller_or_larger == "smaller":
    answer = num_1
    non_answer = num_2
else:
    answer = num_2
    non_answer = num_1

options = [
    {
    "option":answer,
    "correct":True
    },
    {
    "option":answer + 1,
    "correct":False
    },
    {
    "option":answer + 2,
    "correct":False
    },
    {
    "option":non_answer,
    "correct":False
    },
    {
    "option":non_answer - 1,
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
# "The two numbers can be represented as&nbsp;<em>x&nbsp;</em>and&nbsp;<em>x</em>&nbsp;+ 8, since the difference them is 8. Since the two numbers have a sum of 50,&nbsp;<em>x&nbsp;</em>+&nbsp;<em>x</em>&nbsp;+ 8 = 50. This can be rewritten as 2<em>x</em>&nbsp;+ 8 = 50, and the solution is 21. So,&nbsp;<em>x</em>&nbsp;= 21 and&nbsp;<em>x</em>&nbsp;+ 8 = 29.",
# "You may have performed a calculation error and identified 22 as half of 42.",
# "You may have solved 2<em>x</em> + 8 = 50 by subtracted half of 8 instead of 8 from 50.",
# "You may have solved&nbsp;2<em>x</em> + 8 = 50 by adding 8 to 50 instead of subtracting and performing a calculation error in getting 28 instead of 29 as half of 58.",
# "You may have solved an appropriate equation for an unknown value in this situation, but this value represents the larger of the two numbers."
# ]
