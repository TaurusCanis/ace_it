import random

items = [("checking account", "savings account"), ("cat", "dog")]

item_set = random.choice(items)
total_num = random.randrange(300,775,25)

num_item_one = total_num * 3 / 5
num_item_two = round(num_item_one * 3 / 2)
answer = (num_item_one + num_item_two) - total_num

question = f"<p>In a survey, each of {total_num} people was found to have a {item_set[0]}, a {item_set[1]}, or both. If {num_item_one} of these people have {item_set[0]} and {num_item_two} have {item_set[1]}, how many people have both a {item_set[0]} and a {item_set[1]}?&nbsp;</p>\n"


options = [
    {
    "option":answer,
    "correct":True
    },
    {
    "option":answer / 2,
    "correct":False
    },
    {
    "option":total_num / 2,
    "correct":False
    },
    {
    "option":num_item_one,
    "correct":False
    },
    {
    "option":num_item_two,
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

#
# distractor_rationale_response_level = [
#     "You may have taken the number of people who both accounts to be half of the difference between&nbsp;the sum of the numbers of checking account holders and savings account holders and the total number of account holders, but the difference should not be halved.",
#     "Since the sum of the numbers of checking account holders and savings account holders is 600, but only 500 people have at least one of those accounts, there must be 100 people who have both kinds of accounts (the difference between 600 and 500.",
#     "You may have taken the number of people who have both accounts to be half of the number of checking account holders, based on the ratio of 300 to the sum of 300 and 300, but the total number of account holders could only be 450 if 150 of the 300 checking account holders also have savings accounts.",
#     "You may have taken the number of people who have both accounts to be half of the total, based on the ratio of 300 to the sum of 300 and 300, but the total number of account holders could only be 350 if 250 of the 300 checking account holders also have savings accounts.",
#     "You may have taken all account holders to have both kinds of accounts, but it is stated that there are 500 account holders, and so the checking and savings account holders cannot overlap entirely."
# ]
