import numpy as np
from numpy.linalg import solve, matrix_rank

# 3-resistor network
def three_resistors_system(V, R1, R2, R3):
    a = np.array([[1, -1, -1],[R1, R2, 0],[R1, 0,  R3]])
    b = np.array([0, V, V])
    print(f"The rank of the matrix: {matrix_rank(a)}")
    if matrix_rank(a) == 3:
        x = solve(a, b)
        print(x)
        print(f"First branch current = {x[0]}")
        print(f"Second branch current = {x[1]}")
        print(f"Third branch current = {x[2]}")
    elif matrix_rank(a) == 2:
        print("Infinite number of solutions")
    else:
        print("No solution")

# beam force balance system
def three_forces_beam(F, distance_between_a_and_force, beam_length):
    A = np.array([[1, 0, 0],[0, 1, 1],[0, 0,  beam_length]])
    B = np.array([0, F, (F*distance_between_a_and_force)])
    print(f"The rank of the matrix: {matrix_rank(A)}")
    if matrix_rank(A) == 3:
        X = solve(A, B)
        print(X)
        print(f"Horizontal force at A = {X[0]}")
        print(f"Vertical force at A = {X[1]}")
        print(f"Vertical force at B = {X[2]}")
    elif matrix_rank(A) == 2:
        print("Infinite number of solutions")
    else:
        print("No solution")

selection = input("Which system do you want to solve  3-resistor network or 3 forces on a beam (R/B): ").capitalize().strip()

if selection == "R":
    V = float(input("Enter voltage (V): "))
    R1 = float(input("Enter R1 (Ω): "))
    R2 = float(input("Enter R2 (Ω): "))
    R3 = float(input("Enter R3 (Ω): "))
    three_resistors_system(V, R1, R2, R3)
elif selection == "B":
    F = float(input("Enter force: "))
    distance_between_a_and_force = float(input("Enter distance between A and force: "))
    beam_length = float(input("Enter beam length: "))
    three_forces_beam(F, distance_between_a_and_force, beam_length)
else:
    print("Invalid input")