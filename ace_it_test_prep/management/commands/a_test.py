# from .. import math_Q_1 
from django.core.management.base import BaseCommand
from ace_it_test_prep.models import *
import json
from .question_scripts import (
    math_Q_1, math_T1_Q_2, max_min_of_units,
    frac_percent_decimal, measurement, geometry
)

class Command( BaseCommand):
#This can be used to take in an absolute path to file
    # def add_arguments(self, parser):
    #     parser.add_argument('json_file', type=str)


    def handle( self, *args, **options ):
        max_min_of_units.hard()
        frac_question = frac_percent_decimal.Fraction()
        frac_question.print_question()
        measurement_q = measurement.Measurement()
        measurement_q.create_question(type="max_min")
        # measurement_q.print_question()
        print("measurement_q: ", measurement_q.question_text)
        measurement_q.create_question(type="min_distance")
        # measurement_q.print_question()
        print("measurement_q: ", measurement_q.question_text)
        measurement_q.create_question(type="length_of_split_line_segment")
        print("measurement_q: ", measurement_q.question_text)
        geometry_q = geometry.Geometry()
        geometry_q.create_question(type="create_angles_parallel_lines_transversals")
        print("geometry_q: ", geometry_q.question_text)
# exec(open("math_Q_1.py").read())

