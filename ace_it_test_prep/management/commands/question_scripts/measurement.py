import random
class Measurement():
# NOT FINISHED!!!!
    subtype = "NONE"
    num_options = "NONE"
    num_objects = "NONE"
    max_or_min = "NONE"
    question_text = "NONE"
    solution_text = "NONE"
    difficulty = "medium"
    figure = "NONE"
    
    def create_question(self, *args, **kwargs):
        if kwargs['type'] == 'max_min':
            self.create_max_min(*args, **kwargs)
        elif kwargs['type'] == 'min_distance':
            self.create_min_distance(*args, **kwargs)
        elif kwargs['type'] == 'length_of_split_line_segment':
            self.create_length_of_split_line_segment(*args, **kwargs)
    
    def create_max_min(self, *args, **kwargs):
        self.subtype = "minimization/maximization of units"
        self.difficulty = "hard"
        self.num_options = random.randint(3,10)
        self.num_objects = random.randrange(50, 350, 50)
        self.max_or_min = random.choice(["maximum", "minimum"])
        self.question_text = f"At a central train station, there are {self.num_options} different train routes with \
        trains that leave every 6 minutes, 10 minutes, 12 minutes, and 15 minutes. \
        If each train can hold up to {self.num_objects} passengers, what is the {self.max_or_min} number of passengers \
        who can leave the station on a train in one hour?"

        self.solution_text = "The correct answer is E; 5,000. In one hour, 60 \div 6 = 1060÷6=10, \
            60 \div 10 = 660÷10=6, 60 \div 12 = 560÷12=5, and 60 \div 15 = 460÷15=4 trains \
            that can leave the station on the 4 different train routes. Then there are a total \
            of 10 + 6 + 5 + 4 = 2510+6+5+4=25 trains that leave the station in one hour. \
            Since each train can hold a maximum of 200 passengers, the maximum number of \
            passengers who can leave the station by train in one hour is 25 \times 200 = \
            5,00025×200=5,000."
        return self

    def create_min_distance(self, *args, **kwargs):
        self.subtype = "minimum distance on coordinate plane"
        self.difficulty = "medium"
        self.question_text = "In the figure, \mathit{ABCDEFGH}ABCDEFGH is a regular octagon. \
        Which of the following paths is the shortest distance?"
        self.figure = "Figure needed"
        self.solution_text = "The correct answer is E; 5,000. In one hour, 60 \div 6 = 1060÷6=10, \
        60 \div 10 = 660÷10=6, 60 \div 12 = 560÷12=5, and 60 \div 15 = 460÷15=4 trains that can \
        leave the station on the 4 different train routes. Then there are a total of \
        10 + 6 + 5 + 4 = 2510+6+5+4=25 trains that leave the station in one hour. \
        Since each train can hold a maximum of 200 passengers, the maximum number of \
        passengers who can leave the station by train in one hour is 25 \times 200 = 5,00025×200=5,000."

    def create_length_of_split_line_segment(self, *args, **kwargs):
        self.subtype = "solving for length of split line segments"
        self.difficulty = "medium"
        self.question_text = "In Figure 7, the length of \overline{WY}WY is 22 centimeters, \
        the length of \overline{XZ}XZ is 18 centimeters, and the length of \overline{YZ} YZ is \
        12 centimeters. What is the length, in centimeters, of \overline{WX} WX?"
        self.figure = "Figure needed"
        self.solution_text = "C is the best answer. First, identify the given line segments. \
        WXWX is the segment to calculate. Notice that WX = WY - XYWX=WY−XY and WYWY is given. \
        Calculate XYXY and subtract to get the final answer. XYXY is XZ - YZXZ−YZ or 18 - 12 = \
        618−12=6. Since WX = WY - XY = 22 - 6 = 16WX=WY−XY=22−6=16. C is the answer."

    def print_question(self):
        print(self.question_text)