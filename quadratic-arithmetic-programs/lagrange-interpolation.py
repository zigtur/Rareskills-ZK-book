from scipy.interpolate import lagrange
import numpy as np

x = np.array([1,2,3])
y = np.array([4,12,6])

polyC = lagrange(x, y)

print(polyC)
# -7x^2 + 29x - 18# check that it passes through x = {1,2,3} as expected
print(polyC(1))
# 4.0
print(polyC(2))
# 12.0
print(polyC(3))
# 6.0