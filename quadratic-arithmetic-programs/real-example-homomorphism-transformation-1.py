from scipy.interpolate import lagrange
xs = [1,2,3]
ys = [1,0,0]
print(lagrange(xs, ys))
# 0.5 x^2 - 2.5 x + 3