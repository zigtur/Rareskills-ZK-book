from scipy.interpolate import lagrange
xs = [1,2,3]
ys = [0,0,4]
print(lagrange(xs, ys))
# 2 x^2 - 6 x + 4