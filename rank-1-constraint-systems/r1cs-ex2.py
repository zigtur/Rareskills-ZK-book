import numpy as np

# enter the A B and C from above
A = np.array([[0,0,1,0,0,0,0,0],
              [0,0,0,0,0,0,1,0],
              [0,0,0,0,0,0,0,1]])
              
B = np.array([[0,0,0,1,0,0,0,0],
              [0,0,0,0,1,0,0,0],
              [0,0,0,0,0,1,0,0]])
              
C = np.array([[0,0,0,0,0,0,1,0],
              [0,0,0,0,0,0,0,1],
              [0,1,0,0,0,0,0,0]])

# random values for x, y, z, and u
import random
x = random.randint(1,1000)
y = random.randint(1,1000)
z = random.randint(1,1000)
u = random.randint(1,1000)

# compute the algebraic circuit
out = x * y * z * u
v1 = x*y
v2 = v1*z

# create the witness vector
w = np.array([1, out, x, y, z, u, v1, v2])

# element-wise multiplication, not matrix multiplication
result = C.dot(w) == np.multiply(A.dot(w), B.dot(w))

print("Cw = Aw * Bw:", result.all())