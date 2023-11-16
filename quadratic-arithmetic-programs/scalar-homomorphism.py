import numpy as np
from scipy.interpolate import lagrange

x = np.array([1,2,3])
y_v1 = np.array([1, 2, -1])
poly_v1 = lagrange(x, y_v1)

print(poly_v1)
# -2 x^2 + 7 x - 4
# IMPORTANT: We multiply by a constant here
poly_final = poly_v1 * 3
print(poly_final)
# -6 x^2 + 21 x - 12
print("poly_v1 * 3 =", [poly_final(1), poly_final(2), poly_final(3)])
# [3.0, 6.0, -3.0]
print("y_v1 * 3 =", y_v1 * 3)