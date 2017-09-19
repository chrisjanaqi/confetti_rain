#!/usr/bin/env python3
"""
Python project of BPI's teacher

The goal of this project is to make an animation (list of .svg files) of
auto-generated confetti falling through the image

Author: Chris Janaqi
Creation Date: 2017-09-06
"""

from random import choice, randint


class Confetti:
    """
    Class Confetti :

    Attributes:
        - x (int): abcissa of the center of the confetti
        - y (int): ordinate of the center of the confetti
        - color (str): color of the confetti
        - radius (int): radius of the confetti

    Methods:
        - None for now
    """
    def __init__(self, x, y, r, color):
        """
        Confetti constructor with x, y the position (must be integer)
        and the color (must be a string in the svg convention)
        """
        assert (isinstance(x, int) and isinstance(y, int)
                and isinstance(color, str))
        self.x = x
        self.y = y
        self.radius = r
        self.color = color


class Param:
    """
    Class Param used to stock the parameters of the animation

    Attributes :
        - width (int) : width of the animation (in pixels)
        - height (int) : height of the animation (in pixels)
        - nb_frames (int) : number of frame
        - density (float) : density of the rain with
                            (density == r * nb_confetti / width)
                            with r the radius of one confetti.
                            Indicates how much confetti we should generate per
                            frame
        - colors (vector): list of color to use

    Methods:
        - None for now
    """
    def __init__(self, width, height, nb_frames, density,
                 colors=["red", "green", "blue"]):
        self.width = width
        self.height = height
        self.nb_frames = nb_frames
        self.density = density
        self.colors = colors


def input_param():
    """
    Ask the user for the parameters of the animation to produce :
        - width, height of the animation
        - number of frames
        - density
        - color to use
    """
    print("/!\\ WARNING /!\\")
    print("The previous animation WILL be deleted")
    process = input("Continue (y/n)? ") == 'y'
    if process:
        width = int(input('width ? '))
        height = int(input('height ? '))
        nb_frames = int(input('number of frames ? '))
        density = float(input('density of the generation (float in [0,1]) ? '))
        return Param(width, height, nb_frames, density)
    else :
        return None


def generate_confetti(confettis, param):
    """
    Input : confetti vector, parameters of the animation
    """
    nb_confetti = int(param.width * param.density / 10)
    for _ in range(nb_confetti):
        confettis.append(Confetti(randint(0, param.width), 0, 10,
                                  choice(param.colors)))
    return confettis


def simulate_fall(confettis, param):
    """
    Input : confetti vector

    Simulate the fall of confetti, removing those outside of the screen
    """
    for confetti in confettis:
        confetti.y += 4
        confetti.x += randint(-2,2)
        if confetti.y >= param.height + confetti.radius:
            confettis.pop(confettis.index(confetti))

def draw_image(conffetis, param, index):
    """
    Draw into an svg image the confetti vector
    """
    with open('frames/frame_{}.svg'.format(index), 'w') as frame:
        print('<svg width="{}" height="{}">'.format(param.width, param.height),
              file=frame)
        for confetti in conffetis:
            print('<circle cx="{}" cy="{}" r="{}" fill="{}"/>'
                    .format(confetti.x, confetti.y, confetti.radius, confetti.color),
                  file=frame)
        print('</svg>', file=frame)

def main():
    """
    Main function.
    """
    param = input_param()
    conffetis = []
    if param is not None:
        for i in range(param.nb_frames):
            conffetis = generate_confetti(conffetis, param)
            simulate_fall(conffetis, param)
            draw_image(conffetis, param, i)

    print("main here")


if __name__ == "__main__":
    main()
