from mpl_toolkits.axes_grid.axislines import SubplotZero
from io import BytesIO
import base64
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import numpy as np
import random

def create_graph():
    fig = plt.figure(1)
    ax = SubplotZero(fig, 111)
    ax.set(xlim=(-6, 6), ylim=(-6, 6))
    fig.add_subplot(ax)

    for direction in ["xzero", "yzero"]:
    #     ax.axis[direction].set_axisline_style("-|>")
        ax.axis[direction].set_visible(True)
    #
    for direction in ["left", "right", "bottom", "top"]:
        ax.axis[direction].set_visible(False)

    points = {}

    for i in range(0, 5):
        x = random.randint(-5,5)
        y = random.randint(-5,5)
        plt.scatter(x,y)
        ax.annotate(chr(i + 65), (x, y))
        points[str(chr(i + 65))] = "(" + str(x) + ", " + str(y) + ")"

    ax.set_xticks(np.arange(-5, 6, 1))
    ax.set_yticks(np.arange(-5, 6, 1))
    # plt.show()

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()

    graphic = base64.b64encode(image_png)
    graphic = graphic.decode('utf-8')

    correct_answer_letter = str(chr(random.randint(65,70)))
    correct_answer_value = points[correct_answer_letter]
    question = f"Which point shown in the xy-coordinate plane has the coordinates {correct_answer_value}?"
    print(question)

    return { "graphic": graphic, "question": question, "points": points, "correct_answer_letter": correct_answer_letter }
