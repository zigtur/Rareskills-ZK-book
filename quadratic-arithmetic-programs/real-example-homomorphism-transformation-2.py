from scipy.interpolate import lagrange
xs = [1,2,3]
ys = [0,1,0]
print(lagrange(xs, ys))
# -x^2 + 4 x - 3