import random 
class Fraction():
    subtype_1 = "decimals, percents, fractions"
    subtype_2 = "solving units with rates"
    difficulty = "medium"
    x = random.randrange(15, 400) / 100
    y = random.randrange(2, 5)
    question_text = f"One popcorn kernel weighs {x} grams. \
If a package of popcorn kernels weighs {y} kilograms, \
approximately how many popcorn kernels does the package hold?"

    correct_answer = round(y*1000/x)
    distractor_1 = round(correct_answer / 10)
    distractor_2 = round(correct_answer / 100)
    distractor_3 = round(x * 500)
    distractor_4 = round(x * 5000)

    solution_text = "The correct answer is D; 1,626. Divide 2 \
        kilograms by 1.23 grams after converting the kilograms \
        to grams using 1 kg equals 1,000 g:"

    def print_question(self):
        print(self.question_text)
        print(self.correct_answer)
        print(self.distractor_1)
        print(self.distractor_2)
        print(self.distractor_3)
        print(self.distractor_4)