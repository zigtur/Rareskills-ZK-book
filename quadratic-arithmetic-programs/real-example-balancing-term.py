from numpy import poly1d


a = poly1d([29.5, -87.5, 61])
b = poly1d([-1, 4, 0])
c = poly1d([84.5, -246.5, 171])
t = poly1d([1, -1])*poly1d([1, -2])*poly1d([1, -3])

print("Result: h(x) =", (a * b - c) / t)

# quotient, remainder# (poly1d([-29.5,  28.5]), poly1d([0.]))