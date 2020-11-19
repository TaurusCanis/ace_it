import random, math

rand_num = random.randint(3,9)
plus_minus = random.choice([.5, -.5])
second_num = rand_num + plus_minus
lower_time_limit = min(rand_num, second_num)
upper_time_limit = max(rand_num, second_num)

miles = math.floor(second_num) * random.randint(4,8) * 10

question = f"<p>A truck driver took between {lower_time_limit} and {upper_time_limit} hours to make a {miles}-mile trip. The average speed, in miles per hour, must have been between which of the following two numbers?</p>\n",

print(question)

lower_speed_limit = round(miles / upper_time_limit)
upper_speed_limit = round(miles / lower_time_limit)

answer = f"{lower_speed_limit} and {upper_speed_limit}"

options = [
    {
        "option": answer,
        "correct": True
    },
    {
        "option": f"{upper_speed_limit} and {upper_speed_limit + 5}",
        "correct": False
    },
    {
        "option": f"{lower_speed_limit - 5} and {lower_speed_limit}",
        "correct": False
    },
    {
        "option": f"{lower_speed_limit + 10} and {upper_speed_limit + 10}",
        "correct": False
    },
    {
        "option": f"{lower_speed_limit - 10} and {upper_speed_limit - 10}",
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


{
"label":"48 and 50&nbsp;",
"value":"0"
},
{
"label":"50 and 55&nbsp;",
"value":"1"
},
{
"label":"55 and 58&nbsp;",
"value":"2"
},
{
"label":"58 and 64",
"value":"3"
},
{
"label":"64 and 100&nbsp;",
"value":"4"
}

distractor_rationale = [
"You may have estimated 50 miles per hour as average rate for a 6-hour trip, but the result of dividing 350 by 6 is greater, and the result of dividing by 6 would represent the slowest possible average speed rather than the fastest.",
"You may have estimated 55 miles per hour as average rate for a 6-hour trip, but the result of dividing 350 by 6 is greater, and the result of dividing by 6 would represent the slowest possible average speed rather than the fastest.",
"You may have taken the result of dividing 350 by 6 to represent the maximum speed, but that speed is actually the minimum, since 6 hours is the longest possible trip time, representing the slowest possible speed.",
"The average speed of a vehicle is the ratio of the total distance traveled to the total trip time. The ratio of 350 to 5.5 is \\(63\\frac{7}{11}\\), and the ratio of 350 to 6 is \\(58\\frac{1}{3}\\). So, the average speed much be have been&nbsp;greater than 58 miles per hour but&nbsp;less than 64 miles per hour.",
"You may have taken the result of dividing 350 by 5.5 to represent the minimum speed, but that speed is actually the maximum, since 5.5 hours is the shortest possible trip time, representing the fastest possible speed."
]
