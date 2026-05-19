import numpy as np
import matplotlib.pyplot as plt

def Rz(theta):
    theta_rad = np.deg2rad(theta)
    R = np.array([[np.cos(theta_rad), -np.sin(theta_rad), 0], [np.sin(theta_rad), np.cos(theta_rad), 0], [0, 0, 1]])
    return R

def translation(theta, length):
    theta_rad = np.deg2rad(theta)
    P = np.array([[np.cos(theta_rad) * length, np.sin(theta_rad) * length, 0]])
    return P

def make_T(R, P):
    homogenous_transform = np.eye(4)
    homogenous_transform[0:3, 0:3] = R
    homogenous_transform[0:3, 3] = P
    return homogenous_transform

# links and joints parameters
link1_length = int(input("Enter link 1 length: ").strip())
link2_length = int(input("Enter link 2 length: ").strip())

theta_1 = int(input("Enter joint 1 theta: ").strip())
theta_2 = int(input("Enter joint 2 theta: ").strip())

# Homogenous Matrices
T1_0 = make_T(Rz(theta_1), translation(theta_1, link1_length))
T2_1 = make_T(Rz(theta_2), translation(theta_2, link2_length))
T2_0 = T1_0 @ T2_1
print(f"T1_0:\n{T1_0}\n")
print(f"T2_1:\n{T2_1}\n")
print(f"T2_0:\n{T2_0}\n")

end_effector_position = T2_0[:2, 3]

print(f"end_effector_position:\n{end_effector_position}\n")

# points for plotting
# base point
x0, y0 = 0, 0

# link 1 final point
x1 = T1_0[0, 3]
y1 = T1_0[1, 3]

# end effector point
x2 = T2_0[0, 3]
y2 = T2_0[1, 3]

# Plot links
plt.plot([x0, x1], [y0, y1], 'o-', linewidth=4, label='Link 1')
plt.plot([x1, x2], [y1, y2], 'o-', linewidth=4, label='Link 2')
# Plot end effector
plt.scatter(x2, y2, s=100, label='End Effector')

plt.grid(True)
plt.axis('equal')
plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.xlabel("X")
plt.ylabel("Y")
plt.title("2-Link Planar Arm")
plt.legend()
plt.show()

# plotting workspace
workspace_x = []
workspace_y = []

theta1_range = np.arange(-180, 181, 5)
theta2_range = np.arange(-180, 181, 5)

for theta1 in theta1_range:
    for theta2 in theta2_range:
        T1_0 = make_T(Rz(theta1), translation(theta1, link1_length))
        T2_1 = make_T(Rz(theta2), translation(theta2, link2_length))
        T2_0 = T1_0 @ T2_1
        x = T2_0[0, 3]
        y = T2_0[1, 3]
        workspace_x.append(x)
        workspace_y.append(y)

plt.figure(figsize=(7, 7))
plt.scatter(workspace_x, workspace_y, s=2)
plt.title("Workspace of 2-Link Planar Arm")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.axis('equal')
plt.show()
