import numpy as np
from scipy.interpolate import lagrange

x = np.array([1,2,3])
y_v1 = np.array([1, 0, 1])
y_v2 = np.array([-1, 5, 3])
poly_v1 = lagrange(x, y_v1)
poly_v2 = lagrange(x, y_v2)

print(poly_v1)
# 1 x^2 - 4 x + 4print(poly_v2)
#-4 x^2 + 18 x - 15

poly_v3 = poly_v1 + poly_v2

print(poly_v3)
# -3 x^2 + 14 x - 11
print("poly_v1 + poly_v2 =", [poly_v3(1), poly_v3(2), poly_v3(3)])
# [0.0, 5.0, 4.0]
print("y_v1 + y_v2 =", y_v1 + y_v2)