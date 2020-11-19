import random

whole_or_int = random.choice(["whole numbers", "integers"])
odd_even_consecutive = random.choice(["odd", "even", ""])
find_number = random.choice(["smallest", "second smallest", "second largest", "largest"])
options = []

def set_options(answer_options_list):
    print("fwefafgdgq")
    options.extend([
        {
            "option": answer_options_list[0],
            "correct": True
        },
        {
            "option": answer_options_list[1],
            "correct": False
        },
        {
            "option": answer_options_list[2],
            "correct": False
        },
        {
            "option": answer_options_list[3],
            "correct": False
        },
        {
            "option": answer_options_list[4],
            "correct": False
        }
    ])


if whole_or_int == "whole numbers":
    mean_number = random.randint(11,36)
    if odd_even_consecutive == "even":
        while mean_number % 2 != 0:
            mean_number = random.randint(11,36)
    else:
        while mean_number % 2 == 0:
            mean_number = random.randint(11,36)
    print("odd_even_consecutive: ", odd_even_consecutive)
    print("mean number: ", mean_number)
    if odd_even_consecutive == "odd" or odd_even_consecutive == "even":
        print("even or odd")
        if find_number == "smallest":
            answer = mean_number - 4
            set_options([answer, mean_number, mean_number - 2, mean_number - 3, mean_number - 5])
        elif find_number == "second smallest":
            answer = mean_number - 2
            set_options([answer, mean_number, mean_number - 4, mean_number - 3, mean_number - 5])
        elif find_number == "second largest":
            answer = mean_number + 2
            set_options([answer, mean_number, mean_number + 4, mean_number - 3, mean_number - 5])
        else:
            answer = mean_number + 4
            set_options([answer, mean_number, mean_number + 2, mean_number - 3, mean_number - 5])
    else:
        print("not even or odd")
        if find_number == "smallest":
            answer = mean_number - 2
            set_options([answer, mean_number, mean_number - 1, mean_number - 3, mean_number - 5])
        elif find_number == "second smallest":
            answer = mean_number - 1
            set_options([answer, mean_number, mean_number - 2, mean_number - 3, mean_number - 5])
        elif find_number == "second largest":
            answer = mean_number + 1
            set_options([answer, mean_number, mean_number + 2, mean_number - 3, mean_number - 5])
        else:
            answer = mean_number + 2
            set_options([answer, mean_number, mean_number + 1, mean_number - 3, mean_number - 5])
    print("answer: ", answer)
else:
    mean_number = random.randint(-36,36)
    if odd_even_consecutive == "odd" or odd_even_consecutive == "even":
        print("even odd")
        if find_number == "smallest":
            answer = mean_number - 4
            print("SET")
            set_options([answer, mean_number, mean_number - 2, mean_number - 3, mean_number - 5])
        elif find_number == "second smallest":
            answer = mean_number - 2
            set_options([answer, mean_number, mean_number - 4, mean_number - 3, mean_number - 5])
        elif find_number == "second largest":
            answer = mean_number + 2
            set_options([answer, mean_number, mean_number + 4, mean_number + 3, mean_number + 5])
        else:
            answer = mean_number + 4
            set_options([answer, mean_number, mean_number + 2, mean_number + 3, mean_number + 5])
    else:
        print("whole")
        if find_number == "smallest":
            answer = mean_number - 2
            set_options([answer, mean_number, mean_number - 1, mean_number - 3, mean_number - 5])
        elif find_number == "second smallest":
            answer = mean_number - 1
            set_options([answer, mean_number, mean_number - 2, mean_number - 3, mean_number - 5])
        elif find_number == "second largest":
            answer = mean_number + 1
            set_options([answer, mean_number, mean_number + 2, mean_number - 3, mean_number - 5])
        else:
            answer = mean_number + 2
            set_options([answer, mean_number, mean_number + 1, mean_number - 3, mean_number - 5])

question = f"<p>If the mean of five consecutive {odd_even_consecutive} {whole_or_int} is {mean_number}, what is the {find_number} of these five numbers?</p>\n\n<p>&nbsp;</p>\n"




distractor_rationale = [
    "You may have subtracted 5 twice from 18, but the smallest value should be 2 less than the middle value in the set of numbers.",
    "You may have subtracted 3 twice from 18, but the smallest value should be 2 less than the middle value in the set of numbers.",
    "In a set of five consecutive numbers, the mean and the median must be the same. So, the median or third number in the set is 18. The next smallest number is 17, and the smallest number is 16.",
    "You identified the second smallest number, which is one less than the mean and median of the set of numbers, 18.",
    "You may have taken the mean to be the lowest value in the set, but the mean in&nbsp;a set of five consecutive numbers, the mean must be the middle value."
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
