from py_ecc.bn128 import G1, multiply, neg, is_inf, Z1, eq, add

# pick a field element
x = 12345678# generate the point
p = multiply(G1, x)

# invert
p_inv = neg(p)

# every element added to its inverse produces the identity element
assert is_inf(add(p, p_inv))

# Z1 is just None, which is the point at infinity
assert Z1 is None

# special case: the inverse of the identity is itself
assert eq(neg(Z1), Z1)