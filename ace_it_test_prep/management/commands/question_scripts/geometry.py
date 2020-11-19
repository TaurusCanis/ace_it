import random
class Geometry():
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
        if kwargs['type'] == 'create_angles_parallel_lines_transversals':
            self.create_angles_parallel_lines_transversals(*args, **kwargs)
        # elif kwargs['type'] == 'min_distance':
        #     self.create_min_distance(*args, **kwargs)
        # elif kwargs['type'] == 'length_of_split_line_segment':
        #     self.create_length_of_split_line_segment(*args, **kwargs)

    def create_angles_parallel_lines_transversals(self, *args, **kwargs):
        self.subtype = "angles parallel lines transversals"
        self.difficulty = "easy"
        self.num_options = random.randint(3,10)
        self.num_objects = random.randrange(50, 350, 50)
        self.max_or_min = random.choice(["maximum", "minimum"])
        self.question_text = f"In Figure 5, if line MM is parallel to line NN, what is \
        the measure of angle Y?Y?"

        self.solution_text = "The correct answer is B; 75^{\circ}75. The angle that \
        measures 105^{\circ}105 forms a linear pair with the angle that is an alternate \
        exterior angle to angle YY. Then the alternate exterior angle measures \
        180^{\circ} - 105^{\circ} = 75^{\circ}180 −105 =75. Since alternate exterior \
        angles are congruent, then angle YY also measures 75^{\circ}75."

    def unit_rate_of_cost(self, *args, **kwargs):
        self.subtype = "determining unit rate of cost"
        self.difficulty = "easy"
        self.num_options = random.randint(3,10)
        self.num_objects = random.randrange(50, 350, 50)
        self.max_or_min = random.choice(["maximum", "minimum"])
        self.question_text = f"A rectangular yard 65 feet long and 20 feet wide is to be \
        covered with sod. If the total cost of the sod is $7,800, what is the cost of the \
        sod per square foot?"

        self.solution_text = "E is the best answer. The cost of sod per square foot will be \
        the total cost ($7,800) divided by the area. Since the area is a rectangle, the area \
        is equal to length times width: 65 \times 2065×20, or 1300 square feet. Therefore, the \
        sod will cost \$\frac {7,800}{1300} = \$6$ 1300 7,800 =$6 per square foot."

    def area_perim_complex_polygons(self, *args, **kwargs):
        self.subtype = "area and perimeter of complex polygons"
        self.difficulty = "hard"
        self.figure = "figure needed"
        self.num_options = random.randint(3,10)
        self.num_objects = random.randrange(50, 350, 50)
        self.max_or_min = random.choice(["maximum", "minimum"])
        self.question_text = f"Find the area of the irregular shape below."

        #NOTE: diagram needed for solution
        self.solution_text = "The correct answer is B; 80. Divide the diagram into the rectangular \
        sections shown below. The bold numbers show the area of each rectangular region, found \
        using the formula for the area of a rectangle, A = lwA=lw, where l =l= the length of the \
        rectangle, and w =w= the width of the rectangle. Then the area of the irregular shape is \
        the sum of all of the sections:21 + 3 + 18 + 38 = 8021+3+18+38=80."

    def line_segments_multiple_midpoints(self, *args, **kwargs):
        self.subtype = "line segments split by multiple midpoints"
        self.difficulty = "medium"
        self.figure = "figure needed"
        self.num_options = random.randint(3,10)
        self.num_objects = random.randrange(50, 350, 50)
        self.max_or_min = random.choice(["maximum", "minimum"])
        self.question_text = f"On Figure 3, point WW will be located at the midpoint of side \
        ACAC and point ZZ will be located at the midpoint of side BABA. Which lettered point \
        will be located on the line segment WZWZ?"

        self.solution_text = "The correct answer is B; E. Since the midpoint of a side is located \
        at a point halfway between the endpoints, point WW is located halfway between points AA \
        and CC, and point ZZ is located halfway between points AA and BB. Drawing line segment \
        WZWZ shows that only point EE is located on this line segment."

    def min_distance_plane(self, *args, **kwargs):
        self.subtype = "minimum distance on coordinate plane"
        self.difficulty = "hard"
        self.figure = "figure needed"
        self.num_options = random.randint(3,10)
        self.num_objects = random.randrange(50, 350, 50)
        self.max_or_min = random.choice(["maximum", "minimum"])
        self.question_text = f"The coordinates of triangle XYZXYZ are: X (1, 1)X(1,1), \
        Y (6, 6)Y(6,6), and Z (6, 1)Z(6,1). What is the length of line XYXY?"

        self.solution_text = "The correct answer is B; 5\sqrt{2}5 2. After graphing each \
        point given, the horizontal distance between XX and YY is 5 units, and the vertical \
        distance between XX and YY is 5 units. Using Pythagorean Theorem, a^{2} + b^{2} = c^{2}a \
        2+b 2=c 2, where aa and bb are the horizontal and vertical distances respectively, \
        the distance, cc, between XX and YY is 5^{2} + 5^{2} = c^{2}5 2+5 2=c 2. \
        Then c^{2} = 25 + 25 = 50c 2=25+25=50, and c = \sqrt {50} = 5\sqrt {2}c= 50=5 2 units."
