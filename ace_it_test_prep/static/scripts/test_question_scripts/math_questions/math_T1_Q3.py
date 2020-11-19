import random
denom = random.randint(3,5)
denom = denom * 1000 + random.randint(16,225)
num = denom * random.choice([20, 30, 40]) - random.randint(1512, 2909)

question = f"<p class=\"text-center\">\\(\\frac{{{num}}}{{{denom}}}\\ \\)</p>\n\n<p>Which of the following numbers is closest in value to the fraction above?</p>\n"
print("num: ", num)
print("denom: ", denom)
print(question)

answer = round(num / denom, -1)
print("answer: ", answer)

options = [
    {
        "option": answer,
        "correct": True
    },
    {
        "option": round(denom, -2),
        "correct": False
    },
    {
        "option": round(num / (denom / 1000), -1),
        "correct": False
    },
    {
        "option": round(num, -3),
        "correct": False
    },
    {
        "option": round(num, -4),
        "correct": False
    }
]

{
"label":"30&nbsp;",
"value":"0"
},
{
"label":"2,900&nbsp;",
"value":"1"
},
{
"label":"30,000&nbsp;",
"value":"2"
},
{
"label":"85,000&nbsp;",
"value":"3"
},
{
"label":"90,000&nbsp;",
"value":"4"
}

[
"The numerator of the fraction can be rounded to 90,000 and the denominator can be rounded to 3,000. The ratio of 90,000 to 3,000 is equivalent to \\(\\frac{90}{3}\\), which equals 30.",
"You estimated a value close to that of the given denominator, but the value of the fraction is based on the ratio of the numerator to the denominator.",
"You found the ratio of 90,000 to 3 instead of 3,000.",
"You may have estimated the value by rounding the numerator down, but the value of the fraction is based on the ratio of the numerator to the denominator.",
"You may have estimated the value by rounding the numerator up, but the value of the fraction is based on the ratio of the numerator to the denominator."
]

random.shuffle(options)
for option in options:
    print(option["option"])
