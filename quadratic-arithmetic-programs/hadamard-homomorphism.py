import numpy as np
from scipy.interpolate import lagrange

x = np.array([1,2,3])
y_v1 = np.array([1, -1, 2])
y_v2 = np.array([2, 2, -2])
poly_v1 = lagrange(x, y_v1)
poly_v2 = lagrange(x, y_v2)

print(poly_v1)
# 2.5 x^2 - 9.5 x + 8print(poly_v2)
# -2 x^2 + 6 x - 2

poly_v3 = poly_v1 * poly_v2
print(poly_v3)
# -5 x^4 + 34 x^3 - 78 x^2 + 67 x - 16
print("poly_v1 * poly_v2 =", [poly_v3(1), poly_v3(2), poly_v3(3)])
# [2.0, -2.0, -4.0]
print("y_v1 * y_v2 =", y_v1 * y_v2)
