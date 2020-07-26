import random

names = ["Gerald", "Sally"]
name = random.choice(names)

base_rate = random.randint(6,9)
bonus_rate = base_rate + 1

num_hours = random.randint(8,12)
total_hours = num_hours + random.randint(3, 7)

question = f"<p>{name} earns a base hourly rate of ${base_rate} per hour at his&nbsp;job. However, if {name} works more than {num_hours} hours in a week, {name} earns ${bonus_rate} per hour for each hour {name} works after the first {num_hours} hours. How much money does {name} earn if {name} works {total_hours} hours in one week?&nbsp;</p>\n"

base_pay = base_rate * num_hours
bonus_pay = bonus_rate * (total_hours - num_hours)

answer = base_pay + bonus_pay

options = [
    {
    "option": answer,
    "correct": True
    },
    {
    "option": base_rate * total_hours,
    "correct": False
    },
    {
    "option": bonus_rate * (total_hours - 1),
    "correct": False
    },
    {
    "option": (bonus_rate * num_hours) + (base_rate * (total_hours - num_hours)),
    "correct": False
    },
    {
    "option": bonus_rate * total_hours,
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
# "You applied the $8 per hour rate to all 16 hours, overlooking the increase in pay for each hour worked after the first 10 hours.",
# "Gerald's total pay for the week is based on earning $8 per hour for 10 hours and $9 per hour for the additional 6 hours (since 10 + 6 = 16). So, his total pay is the sum of $80 (10&nbsp;× 8 = 80) and $54 (6&nbsp;× 9 = 54), $134.",
# "You applied the $9 per hour rate to a total of 15 hours instead of 16, overlooking the lower rate for the first 10 hours.",
# "You applied the $9 per hour rate for the first 10 hours and the $8 per hour rate for the last 6 hours, but those rates should be swapped with each other.",
# "You applied the $9 per hour rate to all 16 hours, overlooking the lower rate for the first 10 hours."
# ]
