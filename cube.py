#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""© Ihor Mirzov, 2022.
Rubik's cube model. Classes define cube's faces and colors.
"""

from enum import Enum


class Color(Enum):
    """Cube's colors are designated by one letter."""
    RED = 'R' # FRONT face
    ORANGE = 'O' # BACK face
    BLUE = 'B' # LEFT face
    GREEN = 'G' # RIGHT face
    YELLOW = 'Y' # UP face
    WHITE = 'W' # DOWN face


class Cube:
    """Rubik's cube. Is modeled as a set of faces."""

    def __init__(self):
        """Create assembled cube."""
        self.FRONT = Face(Color.RED)
        self.BACK = Face(Color.ORANGE)
        self.LEFT = Face(Color.BLUE)
        self.RIGHT = Face(Color.GREEN)
        self.UP = Face(Color.YELLOW)
        self.DOWN = Face(Color.WHITE)
        self.faces = [
            self.FRONT, self.BACK,
            self.LEFT, self.RIGHT,
            self.UP, self.DOWN
        ]

    def count(self):
        """Count correctly assembled colors."""
        return sum(f.count() for f in self.faces)

    def is_assembled(self):
        """Check if cube is assembled."""
        for f in self.faces:
            if not f.is_assembled():
                return False
        return True

    def print(self):
        """Print cube."""
        print('FRONT    BACK     LEFT     RIGHT    UP       DOWN')
        for row in range(3):
            for f in self.faces:
                f.print_row(row)
            print()
        print()

    def print_colored(self):
        # TODO: implement
        pass


class Face:
    """Cube's face. Consists of 9 colors.
    In methods below 'col' and 'row' are corresponding
    column and row indexes/numbers.
    Indexes of the face colors are as follows:
    0 1 2
    3 4 5
    6 7 8
    """

    def __init__(self, color):
        """On creation, all cells are filled with the same color."""
        self.colors = [color, ] * 9
        self.origin_color = color
    
    def count(self):
        """Count correctly assembled colors."""
        return sum(1 for c in self.colors if c == self.origin_color)

    def rotate_cw(self):
        """Change face colors during clockwise (CW) rotation."""
        l = [
            self.colors[6],
            self.colors[3],
            self.colors[0],
            self.colors[7],
            self.colors[4],
            self.colors[1],
            self.colors[8],
            self.colors[5],
            self.colors[2],
        ]
        self.colors = l

    def rotate_cc(self):
        """Change face colors during counterclockwise (CC) rotation."""
        l = [
            self.colors[2],
            self.colors[5],
            self.colors[8],
            self.colors[1],
            self.colors[4],
            self.colors[7],
            self.colors[0],
            self.colors[3],
            self.colors[6],
        ]
        self.colors = l

    def get_row(self, row):
        """Get colors of the face's row."""
        return [self.colors[row * 3 + col] for col in range(3)]

    def get_col(self, col):
        """Get colors of the face's column."""
        return [self.colors[row * 3 + col] for row in range(3)]

    def set_row(self, row, colors):
        """Set colors of the face's row, len(colors) = 3."""
        for col in range(3):
            self.colors[row * 3 + col] = colors[col]

    def set_col(self, col, colors):
        """Set colors of the face's column, len(colors) = 3."""
        for row in range(3):
            self.colors[row * 3 + col] = colors[row]

    def is_assembled(self):
        """Check if whole the face has the same color."""
        c = self.colors[0]
        for i in range(1, len(self.colors)):
            if self.colors[i] != c:
                return False
        return True

    def print_row(self, row):
        """Print colors of the face's row."""
        s = ' '.join(self.colors[row * 3 + col].value for col in range(3))
        print(s.ljust(9), end='')


if __name__ == '__main__':
    from rotation import Rotation, Directions
    c = Cube()
    d = Directions.FCW
    r = Rotation(c, d)
    c = r.run()
    print(c.count())
