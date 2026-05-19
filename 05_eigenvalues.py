import numpy as np
from numpy.linalg import eig
import matplotlib.pyplot as plt

# get eigen value and eigen vector
A = np.array([[2, -12], [1 , -5]])
print(A)

eigen_values, eigen_vectors = eig(A)

for i in eigen_values:
    print(f"Eigen value: {i}")
print(f"Eigen vectors:\n{eigen_vectors}")

# test the eigen value and corresponding eigen vector
print("\nTested Eigen value and Eigen vector:")
eigen_value = eigen_values[0]
eigen_vector = eigen_vectors[:, 0]
print(f"Eigen value: {eigen_value}")
print(f"Eigen vector:\n{eigen_vector.reshape(2,1)}")

left = A.dot(eigen_vector)
right = eigen_value * eigen_vector

print(np.allclose(left, right))

# stable and unstable systems
# stable system — all eigenvalues have negative real parts
A_stable = np.array([[-2, 1], [-1, -3]])

# Unstable system — at least one eigenvalue has positive real part
A_unstable = np.array([[2, 1], [1, 3]])

for mat, name in [(A_stable, "Stable"), (A_unstable, "Unstable")]:
    vals, _ = eig(mat)
    is_stable = all(np.real(vals) < 0)
    print(f"{name} system eigenvalues: {vals}, Stable: {is_stable}")

# plotting random vectors and eigen vectors
plt.figure(figsize=(8, 8))
np.random.seed(1)

for _ in range(8):

    x = np.random.uniform(-4, 4, 2)
    Ax = A @ x
    plt.quiver(0, 0,x[0], x[1],angles='xy',scale_units='xy',scale=1,color='blue',alpha=0.6)

    plt.quiver(0, 0,Ax[0], Ax[1],angles='xy',scale_units='xy',scale=1,color='red',alpha=0.6)

for i in range(len(eigen_values)):

    v = eigen_vectors[:, i]
    v_scaled = 3 * v
    Av = A @ v_scaled

    plt.quiver(0, 0,v_scaled[0], v_scaled[1],angles='xy',scale_units='xy',scale=1,color='green',linewidth=3,label='Eigenvector' if i == 0 else "")
    plt.quiver(0, 0,Av[0], Av[1],angles='xy',scale_units='xy',scale=1,color='purple',linewidth=3,label='A @ Eigenvector' if i == 0 else "")

plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.xlim(-15, 15)
plt.ylim(-15, 15)
plt.grid(True)
plt.title("Eigenvectors vs Random Vectors")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.gca().set_aspect('equal')
plt.show()
