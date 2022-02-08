#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""© Ihor Mirzov, 2022.
Rubik's cube model and solver.
Main module. Run program here.
"""

from cube import Cube
from rotation import Rotation, recognize_rotations
import solver


def main():
    """Test cube's rotations."""
    c = Cube()
    # c.print() # assembled cube

    # Mix the cube
    string = "D' F R L' U"
    directions = recognize_rotations(string)
    for d in directions:
        r = Rotation(c, d)
        c = r.run()
    # c.print() # mixed cube

    # Solve the cube
    if not c.is_assembled():
        solver.run(c)
    else:
        raise Exception('Cube is already assembled.')


if __name__ == '__main__':
    main()
