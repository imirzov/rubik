#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Solve the cube with a brute-force method.
5 rotations take about 16 seconds to calculate."""

from cube import Cube
from rotation import Directions, Rotation


def maxcalls():
    global MAXDEPTH
    summa = 0
    for d in range(MAXDEPTH):
        summa += 12**d
    return summa


# TODO
allowed_sequences = [
    "R U R' U R U2 R'", # Sune
    "R U2 R' U' R U' R'", # Anti-Sune
    "R' F R F'", # Sledgehammer
    "R U R' U'", # Sexy Move
    "U R U' R'", # Reverse Sexy
    # "M2 U M U2 M' U M2", # U Perms
    # "M2 U' M U2 M' U' M2", # U Perms
    "R U R' U R' F R2 U' R' U' R U R' F'", # T Perm
    "R' U L' U2 R U' R' U2 R L", # J Perms
    "L' U' L F L' U' L U L F' L2' U L U", # J Perms
    "R U R' F' R U R' U' R' F R2 U' R' U'", # J Perms
    # "M2' U' M2' U2' M2' U' M2'", # H Perm
    "R U R' U' R' F R F'", # Key
    "F R U R' U' F'", # T
    "F (R U R' U') (R U R' U') F'", # Bottlecap
    "F U R U' R' U R U' R' F'", # Bottlecap
    # "M2 E2 S2", # Checkerboard
    "R2 L2 U2 D2 F2 B2", # Checkerboard
    # "M' U' M2' U' M2' U' M' U2 M2' U", # Z Perm
]

class Solution:
    """Solution of the cube. It is a sequence of rotations.
    Rotation is a Directions enum item from rotation.py."""

    def __init__(self):
        self.directions = []
        self.achieved = False
        self.count = 0 # amount of assembled colors

    def as_string(self):
        s = [d.value for d in self.directions]
        return ' '.join(s)
    
    def print(self):
        print(self.as_string())

    def compare_with(self, solution):
        """Compare this solution
        with the best one defined in a global variable."""
        if type(solution) != Solution:
            raise TypeError('Solution.compare_with() expects a Solution object.')
        if self.count < solution.count:
            self.directions = solution.directions
            self.count = max(self.count, solution.count)

    def extend(self, another_solution):
        if type(another_solution) != Solution:
            raise TypeError('Solution.extend() expects a Solution object.')
        self.directions.extend(another_solution.directions)

    def next_rotate_direcion_is_ok(self, d0):
        """Add some limitations to the next rotation.
        'd' indexes are numbered from right to left."""

        def equal(*directions):
            """Check if all directions are equal."""
            return all(x.value == directions[0].value for x in directions[1:])

        def is_back(d1, d2):
            """Check if second rotation is the back one for the first."""
            return d1.value == d2.value + "'" or d1.value + "'" == d2.value

        def are_opposite_faces(d1, d2):
            """Check if two rotations are applied to the opposite faces."""
            if d1.name.startswith('F') and d2.name.startswith('B'):
                return True
            elif d1.name.startswith('L') and d2.name.startswith('R'):
                return True
            elif d1.name.startswith('U') and d2.name.startswith('D'):
                return True
            return False

        if self.achieved:
            return False

        if len(self.directions) >= 1:
            d1 = self.directions[-1]

            # Exclude patterns like "F' F"
            if is_back(d0, d1):
                return False

            if len(self.directions) >= 2:
                d2 = self.directions[-2]

                # Exclude patterns like "F F F" and "F' B F"
                if equal(d0, d1, d2):
                    return False
                if are_opposite_faces(d0, d1) and is_back(d0, d2):
                    return False

                if len(self.directions) >= 3:
                    d3 = self.directions[-3]

                    # Exclude patterns like "F F B F", "F B F F"
                    if equal(d0, d2, d3) and are_opposite_faces(d0, d1):
                        return False
                    if equal(d0, d1, d3) and are_opposite_faces(d0, d2):
                        return False

                    # Exclude patterns like "F' B B F"
                    if is_back(d0, d3) and are_opposite_faces(d0, d1) and are_opposite_faces(d0, d2):
                        return False

                    if len(self.directions) >= 4:
                        d4 = self.directions[-4]

                        # Exclude patterns like "F F B B F", "F F B B F'"
                        if equal(d0, d3, d4) and are_opposite_faces(d0, d1) and are_opposite_faces(d0, d2):
                            return False

        return True


MAXDEPTH = 5 # amount of cube rotations in final solution formula
MAXROTATIONS = 12**MAXDEPTH # amount of cube variants
MAXCALLS = maxcalls() # 12^0 + 12^1 + ... + 12^MAXDEPTH
total_rotations = 0 # amount of performed rotations
total_calls = 0 # amount of graph nodes
total_depth = 0 # amount of graph levels
best_solution = Solution()
longest_formula = Solution()


def solve(cube, solution=Solution(), depth=1):
    """Recursive function to find the solution."""

    global longest_formula

    # Check if cube is already assembled
    global best_solution
    if cube.is_assembled():
        solution.achieved = True
        solution.count = cube.count()
        best_solution.compare_with(solution)
        return solution

    global MAXDEPTH, total_depth
    total_depth = max(total_depth, depth)

    global MAXCALLS, total_calls
    if total_calls >= MAXCALLS:
        return
    else:
        total_calls += 1

    global MAXROTATIONS, total_rotations
    for d in list(Directions):

        # Apply rotation and remember the sequence of directions
        if total_rotations >= MAXROTATIONS:
            continue
        else:

            # Add some rules to limit the search space
            if not solution.next_rotate_direcion_is_ok(d):
                continue

            total_rotations += 1
            r = Rotation(cube, d)
            c = r.run()

            s = Solution()
            s.directions = solution.directions + [d]
            s.count = c.count() # count assembled colors
            best_solution.compare_with(s)

            """Check if current solution is the longest one.
            Using it for developing better filters."""
            if len(s.directions) > len(longest_formula.directions):
                longest_formula = s

            # Recursively solve the cube
            if c.is_assembled():
                s.achieved = True
                best_solution = s
                return s
            else:
                if depth + 1 > MAXDEPTH:
                    # Continue with the next rotation on the same level
                    continue 
                else:
                    s = solve(c, s, depth + 1)
                    if s is not None and s.achieved:
                        return s


def run(c=Cube()):
    """Solve the cube."""

    import time
    start_time = time.perf_counter()

    s = solve(c)
    if total_depth > MAXDEPTH:
        print('Too deep,', total_depth)
    if total_calls > MAXCALLS:
        print('Too many calls,', total_calls)
    if total_rotations > MAXROTATIONS:
        print('Too many rotations,', total_rotations)

    print('Best solution - {} colors in place:'.format(best_solution.count))
    print(len(best_solution.directions), 'rotations')
    print(best_solution.as_string())

    if s is None or not s.achieved:
        print('Not solved.')
    else:
        print('Solved', s.achieved)

    print('Longest formula:')
    print(longest_formula.as_string())

    print()
    print('Total depth:', total_depth)
    print('Total calls: {} of max {}'.format(total_calls, maxcalls()))
    print('Total rotations: {} of max {}'.format(total_rotations, 12**total_depth))
    print('Total time: {:.1f} seconds.\n'
        .format(time.perf_counter() - start_time))

    # Amount of possible cube variants in 20 rotations
    print('Possible variants:\n', pow(12, 20))


if __name__ == '__main__':
    run()
