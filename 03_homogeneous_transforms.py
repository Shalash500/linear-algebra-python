import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

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

def make_T(R, T):
    homogenous_transform = np.eye(4)
    homogenous_transform[0:3, 0:3] = R
    homogenous_transform[0:3, 3] = T
    return homogenous_transform

def apply_T(T, point):
    point_h = np.append(point, 1)
    transformed_point = T @ point_h
    return transformed_point[:3]

def invert_T(T):
    R = T[0:3, 0:3]
    t = T[0:3, 3]
    T_inv = np.eye(4)
    T_inv[0:3, 0:3] = R.T
    T_inv[0:3, 3] = -R.T @ t
    return T_inv

def plot_frame(ax, T, name):
    origin = T[:3, 3]
    x_axis = T[:3, :3] @ np.array([1, 0, 0])
    y_axis = T[:3, :3] @ np.array([0, 1, 0])
    z_axis = T[:3, :3] @ np.array([0, 0, 1])
    ax.quiver(origin[0], origin[1], origin[2],x_axis[0], x_axis[1], x_axis[2],color='r')
    ax.quiver(origin[0], origin[1], origin[2],y_axis[0], y_axis[1], y_axis[2],color='g')
    ax.quiver(origin[0], origin[1], origin[2],z_axis[0], z_axis[1], z_axis[2],color='b')
    ax.text(origin[0],origin[1],origin[2],name)

rotation_matrix = None
point_x, point_y, point_z = map(int, input("Enter the point coordinates separated by space: ").split())
original_point = np.array([point_x, point_y, point_z])
selected_axis = input("What axis do you want to rotate the point around(x/y/z)? ").lower().strip()
angle = int(input("What is the angle to rotate the point? "))
if selected_axis == "x":
    rotation_matrix = Rx(angle)
elif selected_axis == "y":
    rotation_matrix = Ry(angle)
elif selected_axis == "z":
    rotation_matrix = Rz(angle)

translation_x, translation_y, translation_z = map(int, input("Enter the translation separated by space: ").split())
translation_matrix = np.array([translation_x, translation_y, translation_z])
homogenous_matrix = make_T(rotation_matrix, translation_matrix)
new_point = apply_T(homogenous_matrix, original_point)

print(f"The homogenous matrix:\n{homogenous_matrix}")
print(f"\nThe original point:\n{original_point.transpose()}")
print(f"\nThe new point:\n{new_point.transpose()}")

homogenous_transform_inverse = invert_T(homogenous_matrix)
print(f"\nThe homogenous transform inverse:\n{homogenous_transform_inverse}")

print("\nCheck inverse correctness:")
print(np.allclose(homogenous_transform_inverse @ homogenous_matrix,np.eye(4)))

print("\n========== CHAINING TRANSFORMS ==========")

# First transform
R1 = Rz(90)
t1 = np.array([1, 0, 0])

T1 = make_T(R1, t1)

# Second transform
R2_matrix = Rx(90)
t2 = np.array([0, 2, 0])

T2 = make_T(R2_matrix, t2)

# Chain transforms
T_total_1 = T1 @ T2
T_total_2 = T2 @ T1

print("\nT1 @ T2:")
print(T_total_1)

print("\nT2 @ T1:")
print(T_total_2)

print("\nfirst and second transform equal? ")
print(np.allclose(T_total_1, T_total_2))


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
plot_frame(ax, np.eye(4), "World")
plot_frame(ax, homogenous_matrix, "Transformed")
ax.set_xlim([-5, 5])
ax.set_ylim([-5, 5])
ax.set_zlim([-5, 5])
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
plt.show()
