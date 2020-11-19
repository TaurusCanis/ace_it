import random
def q_2():
    dim_x = random.randint(2,10)
    dim_y = random.randint(4,8)
    dim_z = random.randint(6,8)
    volume = dim_x * dim_y * dim_z
    question = f"<p>A rectangular prism has a volume of {volume} cubic meters. Which of the following could be its dimensions?</p>\n"
    print(question)
    answer = f"{dim_x} m by {dim_y} m by {dim_z} m"
    options = [
        {
            "option": answer,
            "correct": True
        },
        {
            "option": f"{dim_x / 2} m by {dim_y - 1} m by {dim_z} m",
            "correct": False
        },
        {
            "option": f"{dim_x + 1} m by {dim_y / 2} m by {dim_z} m",
            "correct": False
        },
        {
            "option": f"{dim_x} m by {dim_y} m by {dim_z - 2} m",
            "correct": False
        },
        {
            "option": f"{dim_x} m by {dim_y * 2} m by {dim_z + 1} m",
            "correct": False
        },
    ]

    random.shuffle(options)
    letter_index = 65
    for option in options:
        print(chr(letter_index) + ": " + option["option"])
        letter_index += 1

    user_response = input("Choose and answer option: ")
    if options[ord(user_response.upper()[0]) - 65]["correct"]:
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print("Correct answer: ", answer)

    distractor_rationale = [
    "You may have made a calculation error when multiplying the dimensions, as the product of 4, 7 and 9 is 252.",
    "You may have made a calculation error when multiplying the dimensions, as the product of 8, 8 and 4 is 256.",
    "The volume of a rectangular prism is the product of the length, width, and height, and the product of the 8, 9, and 4 is 288.",
    "You may have made a calculation error when multiplying the dimensions, as the product of 12, 6 and 2 is only half of 288.",
    "You may have made a calculation error when multiplying the dimensions, as the product of 12, 12 and 4 is twice 288."
    ]
