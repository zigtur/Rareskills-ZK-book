import numpy as np
import random

# Define the matrices
A = np.array([[0,0,1,0]])
B = np.array([[0,0,0,1]])
C = np.array([[-2,1,0,0]])

# pick random values to test the equation
x = random.randint(1,1000)
y = random.randint(1,1000)
out = x * y + 2# witness vector
w = np.array([1, out, x, y])

# check the equality
result = C.dot(w) == np.multiply(A.dot(w),B.dot(w))
print("Cw = Aw * Bw:", result.all())