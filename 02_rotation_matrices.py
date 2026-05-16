import numpy as np
import matplotlib.pyplot as plt

def R2(theta):
    theta_rad = np.deg2rad(theta)
    R = np.array([[np.cos(theta_rad), -np.sin(theta_rad)], [np.sin(theta_rad), np.cos(theta_rad)]])
    return R

def two_dimension_plot(V_original, V_rotated, angle):
    plt.figure(figsize=(5, 5))
    plt.quiver(0, 0, V_original[0], V_original[1], angles='xy', scale_units='xy', scale=1, color='blue',label='Original Vector')
    plt.quiver(0, 0, V_rotated[0], V_rotated[1], angles='xy', scale_units='xy', scale=1, color='red',label=f'Rotated {angle}°')
    plt.xlim(-10.0, 10.0)
    plt.xticks(np.arange(-10, 11, 1))
    plt.ylim(-10.0, 10.0)
    plt.yticks(np.arange(-10, 11, 1))
    plt.axhline(0, color='black', lw=1)
    plt.axvline(0, color='black', lw=1)
    plt.legend()
    plt.grid(True)
    plt.show()


def Rx(theta):
    theta_rad = np.deg2rad(theta)
    R = np.array([[1, 0, 0], [0, np.cos(theta_rad), -np.sin(theta_rad)], [0, np.sin(theta_rad), np.cos(theta_rad)]])
    return R

def Ry(theta):
    theta_rad = np.deg2rad(theta)
    R = np.array([[np.cos(theta_rad), 0, np.sin(theta_rad)], [0, 1, 0], [-np.sin(theta_rad), 0, np.cos(theta_rad)]])
    return R

def Rz(theta):
    theta_rad = np.deg2rad(theta)
    R = np.array([[np.cos(theta_rad), -np.sin(theta_rad), 0], [np.sin(theta_rad), np.cos(theta_rad), 0], [0, 0, 1]])
    return R

angle = int(input("What is the angle to rotate the vector? "))

dimension = input("What is the dimension of the vector(2/3)? ").strip()

if dimension == "2":
    vector_x, vector_y = map(int, input("Enter the vector separated by space: ").split())
    rotation_matrix = R2(angle)
    vector_original = np.array([vector_x, vector_y])
    vector_rotated = rotation_matrix.dot(vector_original)
    print("The original vector is", vector_original)
    print("The rotated vector is:", vector_rotated)
    two_dimension_plot(vector_original, vector_rotated, angle)

else:
    vector_x, vector_y, vector_z = map(int, input("Enter the vector separated by space: ").split())
    vector_original = np.array([vector_x, vector_y, vector_z])
    selected_axis = input("What axis do you want to rotate the vector around(x/y/z)? ").lower().strip()
    print("The original vector is", vector_original)
    if selected_axis == "x":
        rotation_matrix = Rx(angle)
        vector_rotated = rotation_matrix.dot(vector_original)
        print("The rotated vector is:", vector_rotated)
    elif selected_axis == "y":
        rotation_matrix = Ry(angle)
        vector_rotated = rotation_matrix.dot(vector_original)
        print("The rotated vector is:", vector_rotated)
    elif selected_axis == "z":
        rotation_matrix = Rz(angle)
        vector_rotated = rotation_matrix.dot(vector_original)
        print("The rotated vector is:", vector_rotated)


print("========================================")
# Orthogonality verification: R @ R.T should equal identity
print(np.allclose(Rx(45) @ Rx(45).T, np.eye(3)))  # True
print(np.allclose(Ry(30) @ Ry(30).T, np.eye(3)))  # True
print(np.allclose(Rz(60) @ Rz(60).T, np.eye(3)))  # True

print("========================================")
# Composition: Rz(45) @ Ry(30) is NOT equal to Ry(30) @ Rz(45)
result1 = Rz(45) @ Ry(30)
result2 = Ry(30) @ Rz(45)
print(result1)
print(result2)
print(np.allclose(result1, result2))  # False — order matters
