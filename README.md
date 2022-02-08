# Rubik's cube solver 

Rubik's cube model and solver.

**cube.py** - Rubik's cube model. Classes define cube's faces and colors. Cube is modeled as a set of faces. Face consists of 9 colors indexed from 0 to 8. Colors are designated by one letter.

**rotation.py** - rotations which could be performed on the cube. Program can recognize international formulas designating face rotations. Middle layer rotation is not jet supported.

**solver.py** - solve the cube with a brute-force method. To find a solution a recursive function is used. The function checks all possible rotations, excluding senseless sequences.

A graph with depth of 5 has 12**5=248832 nodes. 5 rotations take about 16 seconds to calculate on my laptop, so 20 rotations will take about 8.5 billion years :) So I'm leaving this task incompleted.
