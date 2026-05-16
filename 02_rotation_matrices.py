import numpy as np
import matplotlib.pyplot as plt

def R2(theta):
    theta_rad = np.deg2rad(theta)
    R = np.array([[np.cos(theta_rad), -np.sin(theta_rad)], [np.sin(theta_rad), np.cos(theta_rad)]])
    return R

angle = int(input("What is the angle to rotate the vector? "))

vector_x, vector_y = map(int, input("Enter the vector separated by space: ").split())

rotation = R2(angle)
vector_original = np.array([vector_x, vector_y])
vector_rotated = rotation.dot(vector_original)

plt.figure(figsize=(5, 5))
plt.quiver(0, 0, vector_original[0], vector_original[1], angles='xy', scale_units='xy', scale=1, color='blue', label='Original Vector')
plt.quiver(0, 0, vector_rotated[0], vector_rotated[1], angles='xy', scale_units='xy', scale=1, color='red', label=f'Rotated {angle}°')
plt.xlim(-10.0, 10.0)
plt.xticks(np.arange(-10, 11, 1))
plt.ylim(-10.0, 10.0)
plt.yticks(np.arange(-10, 11, 1))
plt.axhline(0, color='black', lw=1)
plt.axvline(0, color='black', lw=1)
plt.legend()
plt.grid(True)
plt.show()