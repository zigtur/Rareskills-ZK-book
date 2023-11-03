import numpy as np

# define the matrices
C = np.array([[0,1,0,0]])
A = np.array([[0,0,1,0]])
B = np.array([[0,0,0,1]])

# witness vector
witness = [1, 4223, 41, 103]

# Multiplication is element-wise, not matrix multiplication. # Result contains a bool indicating an element-wise indicator that the equality is true for that element.
result = C.dot(witness) == A.dot(witness) * B.dot(witness)

# check that every element-wise equality is true
print("Cw = Aw * Bw:", result.all())