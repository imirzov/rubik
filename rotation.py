#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""© Ihor Mirzov, 2022.
Actions which could be performed on the cube.

This is how face cells are numbered:
TODO print cube like this in color

        0 1 2
        3 U 5
        6 7 8

0 1 2   0 1 2   0 1 2   0 1 2
3 L 5   3 F 5   3 R 5   3 B 5
6 7 8   6 7 8   6 7 8   6 7 8

        0 1 2
        3 D 5
        6 7 8
"""

import copy
from enum import Enum


class Directions(Enum):
    """Clockwise CW and counterclockwise CC."""
    FCW = "F"; FCC = "F'"
    BCW = "B"; BCC = "B'"
    LCW = "L"; LCC = "L'"
    RCW = "R"; RCC = "R'"
    UCW = "U"; UCC = "U'"
    DCW = "D"; DCC = "D'"


class Rotation:
    """Single rotation of the cube's face.
    Rotate and return cube.
    """

    def __init__(self, cube, direction):
        self.cube = copy.deepcopy(cube)
        self.direction = direction

    def run(self):
        """Rotation function name is constructed
        from the direction designation. Then just call it.
        """
        fname = f'rotate_{self.direction.name[0]}'
        getattr(self, fname)()
        return self.cube

    def rotate_F(self):
        """Affected sides on FRONT face rotation:
        LEFT column 2, UP row 2,
        RIGHT column 0, DOWN row 0.
        """
        L_col2 = self.cube.LEFT.get_col(2)
        U_row2 = self.cube.UP.get_row(2)
        R_col0 = self.cube.RIGHT.get_col(0)
        D_row0 = self.cube.DOWN.get_row(0)

        if self.direction == Directions.FCW:
            # Rotate FRONT face clockwise
            self.cube.FRONT.rotate_cw()
            self.cube.LEFT.set_col(2, D_row0)
            self.cube.UP.set_row(2, L_col2)
            self.cube.RIGHT.set_col(0, U_row2)
            self.cube.DOWN.set_row(0, R_col0)
        elif self.direction == Directions.FCC:
            # Rotate FRONT face counterclockwise
            self.cube.FRONT.rotate_cc()
            self.cube.LEFT.set_col(2, U_row2)
            self.cube.UP.set_row(2, R_col0)
            self.cube.RIGHT.set_col(0, D_row0)
            self.cube.DOWN.set_row(0, L_col2)

    def rotate_B(self):
        """Affected sides on BACK face rotation:
        RIGHT column 2, UP row 0,
        LEFT column 0, DOWN row 2.
        """
        R_col2 = self.cube.RIGHT.get_col(2)
        U_row0 = self.cube.UP.get_row(0)
        L_col0 = self.cube.LEFT.get_col(0)
        D_row2 = self.cube.DOWN.get_row(2)

        if self.direction == Directions.BCW:
            # Rotate BACK face clockwise
            self.cube.BACK.rotate_cw()
            self.cube.RIGHT.set_col(2, D_row2)
            self.cube.UP.set_row(0, R_col2)
            self.cube.LEFT.set_col(0, U_row0)
            self.cube.DOWN.set_row(2, L_col0)
        elif self.direction == Directions.BCC:
            # Rotate BACK face counterclockwise
            self.cube.BACK.rotate_cc()
            self.cube.RIGHT.set_col(2, U_row0)
            self.cube.UP.set_row(0, L_col0)
            self.cube.LEFT.set_col(0, D_row2)
            self.cube.DOWN.set_row(2, R_col2)

    def rotate_L(self):
        """Affected sides on LEFT face rotation:
        BACK column 0, UP col 0,
        FRONT column 0, DOWN col 0.
        """
        B_col0 = self.cube.BACK.get_col(0)
        U_col0 = self.cube.UP.get_col(0)
        F_col0 = self.cube.FRONT.get_col(0)
        D_col0 = self.cube.DOWN.get_col(0)

        if self.direction == Directions.LCW:
            # Rotate LEFT face clockwise
            self.cube.LEFT.rotate_cw()
            self.cube.BACK.set_col(0, D_col0)
            self.cube.UP.set_col(0, B_col0)
            self.cube.FRONT.set_col(0, U_col0)
            self.cube.DOWN.set_col(0, F_col0)
        elif self.direction == Directions.LCC:
            # Rotate LEFT face counterclockwise
            self.cube.LEFT.rotate_cc()
            self.cube.BACK.set_col(0, U_col0)
            self.cube.UP.set_col(0, F_col0)
            self.cube.FRONT.set_col(0, D_col0)
            self.cube.DOWN.set_col(0, B_col0)

    def rotate_R(self):
        """Affected sides on RIGHT face rotation:
        FRONT column 2, UP col 2,
        BACK column 2, DOWN col 2.
        """
        F_col2 = self.cube.FRONT.get_col(2)
        U_col2 = self.cube.UP.get_col(2)
        B_col0 = self.cube.BACK.get_col(0)
        D_col2 = self.cube.DOWN.get_col(2)

        if self.direction == Directions.RCW:
            # Rotate RIGHT face clockwise
            self.cube.RIGHT.rotate_cw()
            self.cube.FRONT.set_col(2, D_col2)
            self.cube.UP.set_col(2, F_col2)
            self.cube.BACK.set_col(0, U_col2)
            self.cube.DOWN.set_col(2, B_col0)
        elif self.direction == Directions.RCC:
            # Rotate RIGHT face counterclockwise
            self.cube.RIGHT.rotate_cc()
            self.cube.FRONT.set_col(2, U_col2)
            self.cube.UP.set_col(2, B_col0)
            self.cube.BACK.set_col(0, D_col2)
            self.cube.DOWN.set_col(2, F_col2)

    def rotate_U(self):
        """Affected sides on UP face rotation:
        LEFT row 0, FRONT row 0,
        RIGHT row 0, BACK row 0.
        """
        L_row0 = self.cube.LEFT.get_row(0)
        F_row0 = self.cube.FRONT.get_row(0)
        R_row0 = self.cube.RIGHT.get_row(0)
        B_row0 = self.cube.BACK.get_row(0)

        if self.direction == Directions.UCW:
            # Rotate UP face clockwise
            self.cube.UP.rotate_cw()
            self.cube.LEFT.set_row(0, F_row0)
            self.cube.FRONT.set_row(0, R_row0)
            self.cube.RIGHT.set_row(0, B_row0)
            self.cube.BACK.set_row(0, L_row0)
        elif self.direction == Directions.UCC:
            # Rotate UP face counterclockwise
            self.cube.UP.rotate_cc()
            self.cube.LEFT.set_row(0, B_row0)
            self.cube.FRONT.set_row(0, L_row0)
            self.cube.RIGHT.set_row(0, F_row0)
            self.cube.BACK.set_row(0, R_row0)

    def rotate_D(self):
        """Affected sides on DOWN face rotation:
        LEFT row 2, FRONT row 2,
        RIGHT row 2, BACK row 2.
        """
        L_row2 = self.cube.LEFT.get_row(2)
        F_row2 = self.cube.FRONT.get_row(2)
        R_row2 = self.cube.RIGHT.get_row(2)
        B_row2 = self.cube.BACK.get_row(2)

        if self.direction == Directions.DCW:
            # Rotate DOWN face clockwise
            self.cube.DOWN.rotate_cw()
            self.cube.LEFT.set_row(2, B_row2)
            self.cube.FRONT.set_row(2, L_row2)
            self.cube.RIGHT.set_row(2, F_row2)
            self.cube.BACK.set_row(2, R_row2)
        elif self.direction == Directions.DCC:
            # Rotate DOWN face counterclockwise
            self.cube.DOWN.rotate_cc()
            self.cube.LEFT.set_row(2, F_row2)
            self.cube.FRONT.set_row(2, R_row2)
            self.cube.RIGHT.set_row(2, B_row2)
            self.cube.BACK.set_row(2, L_row2)


def recognize_rotations(string):
    """Parse a string of moves and return a list of Directions objects.
    The string is something like "U' L' U L U F U' F'".
    Could be without spaces. Understands only side rotations, not middle.
    TODO Implement double rotations parsing like U2, F2' etc.
    """
    directions = {d.value:d for d in list(Directions)}
    rotations = []
    for s in string.replace(' ', ''):
        if s in directions or s == "'":
            if s == "'":
                d = directions[rotations[-1].value + "'"]
                rotations[-1] = d
            else:
                d = directions[s]
                rotations.append(d)
        else:
            raise ValueError('Invalid rotation symbol "{}"'.format(s))
    return rotations


if __name__ == '__main__':
    string = "FF'BB'LL'RR'UU'DD'"
    # string = "U' L' U L U F U' F'"
    for r in recognize_rotations(string):
        print('{}\t{}'.format(r.value, r))
