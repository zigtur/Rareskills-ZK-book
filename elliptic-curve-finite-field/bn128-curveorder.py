from py_ecc.bn128 import curve_order, field_modulus, G1, multiply, eq, add

x = 5 # chosen randomly# This passes
assert eq(multiply(G1, x), multiply(G1, x + curve_order))

# This fails
assert not(eq(multiply(G1, x), multiply(G1, x + field_modulus)))

x = 2 ** 300 + 21
y = 3 ** 50 + 11

# (x + y) == xG + yG
assert eq(multiply(G1, (x + y)), add(multiply(G1, x), multiply(G1, y)))
assert eq(multiply(G1, (x + y) % curve_order), add(multiply(G1, x), multiply(G1, y)))
assert not(eq(multiply(G1, (x + y) % (curve_order - 1)), add(multiply(G1, x), multiply(G1, y))))


