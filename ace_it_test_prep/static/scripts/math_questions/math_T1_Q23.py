import random
from math import sqrt

root = random.randint(2,5)
radicand_exp = random.randint(root + 1, root * 5)

question = f"<p>If &nbsp;\\(a&gt;0\\)&nbsp;, which of the following expressions is equivalent to \\(\\sqrt[{root}]{{a^{radicand_exp}}}\\)&nbsp; ?</p>\n"

coefficient = radicand_exp // root
remainder = radicand_exp % root
answer = f"\\{{a^{coefficient}}}(\\sqrt[{root}]{{a^{remainder}}}\\)"

options = [
    {
    "option": answer,
    "correct": True
    },
    {
    "option": f"\\{{a^{remainder}}}(\\sqrt[{root}]{{a^{coefficient}}}\\)",
    "correct": False
    },
    {
    "option":"\\(a^" + str(eval(f"{radicand_exp} - {root}")) + "\\)",
    "correct": False
    },
    {
    "option":"\\(a^" + str(round(sqrt(radicand_exp))) + "\\)",
    "correct": False
    },
    {
    "option":"\\(a^" + str(eval(f"{radicand_exp} * {root}")) + "\\)",
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

#  "distractor_rationale_response_level":[
# "You found an expression equivalent to&nbsp;\\(\\left(a^9\\right)^4\\) instead of \\(\\sqrt[4]{a^9}\\).",
# "You subtracted 4 from the exponent instead of taking the fourth root, which should involve dividing an exponent by 4.",
# "You used the square root of the exponent, but finding the root in question with involve dividing the exponent by 4.",
# "You factored out the square root instead of the fourth root of \\(a^8\\).&nbsp;",
# "The expression represents the fourth fourth root of&nbsp;\\(a^9\\)<em>.&nbsp;</em>The term&nbsp;\\(a^8\\) can be written as \\(a^8\\left(a\\right)\\),and the fourth root of&nbsp;\\(a^8\\) is \\(a^2\\). So, the square of&nbsp;<em>a</em>&nbsp;is a factor of the original expression, such that \\(\\sqrt[4]{a^9}=\\left(a^2\\right)\\sqrt[4]{a}\\)."
# ]
