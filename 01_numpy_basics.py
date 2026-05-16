import numpy as np
from numpy.linalg import *
# The basics
a = np.arange(15).reshape(3, 5)
print(a)
print("--------------")
print(a.shape)
print("--------------")
print(a.ndim)
print("--------------")
print(a.dtype.name)
print("--------------")
print(a.itemsize)
print("--------------")
print(a.size)

print("======================================")

# Array creation
b = np.array([2,3,4])
print(b)
print("--------------")
print(b.dtype)
print("--------------")
c = np.array([1.5,2.2,3.8])
print(c)
print("--------------")
print(c.dtype)
print("--------------")
d = np.zeros((3,4))
print(d)
print("--------------")
e = np.ones((3,4))
print(e)
print("--------------")
f = np.empty((3,4))
print(f)
print("--------------")
g = np.arange(10, 30, 5)
print(g)
print("--------------")
h = np.eye(3)
print(h)

print("======================================")

# Printing arrays
a = np.arange(6)    # 1-D array
print(a)
print("--------------")
b = np.arange(12).reshape(4, 3)     # 2-D array
print(b)
print("--------------")
c = np.arange(24).reshape(2, 3, 4)  # 3-D array
print(c)

print("======================================")

# Basic operations
a = np.array([20, 30, 40, 50])
b = np.arange(4)
c = a - b
print(c)
print("--------------")
print(b**2)
print("--------------")
A = np.array([[1, 1],[0, 1]])
B = np.array([[2, 0],[3, 4]])
print(A * B)        # elementwise product
print("--------------")
print(A @ B)        # matrix product
print("--------------")
print(A.dot(B))     # matrix product

print("======================================")

# Linear algebra
a = np.array([[1, -1, 0], [1, 0, -1], [-6, 2, 3]])
print(a)
print("--------------")
print(inv(a))       # matrix inverse
print("--------------")
print(a.transpose())    # matrix transpose
print("--------------")
print(det(a))       # matrix determinant
