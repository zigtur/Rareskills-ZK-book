import numpy as np

# 1, out, x, y, v1, v2, v3
L = np.array([
    [0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, -5, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1],
])

R = np.array([
    [0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0],
])

O = np.array([
    [0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 1],
    [0, 1, 0, 0, 0, -1, 0],
])

x = 4
y = -2
v1 = x * x
v2 = v1 * v1         # x^4
v3 = -5*y * y
out = v3*v1 + v2    # -5y^2 * x^2

witness = np.array([1, out, x, y, v1, v2, v3])

print("Result: R1CS witness verification:", all(np.equal(np.matmul(L, witness) * np.matmul(R, witness), np.matmul(O, witness))))