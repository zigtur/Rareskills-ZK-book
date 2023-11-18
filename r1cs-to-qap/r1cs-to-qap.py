import galois
import numpy as np
import functools as ft

## R1CS

# 1, out, x, y, v1, v2, v3
L = np.array([
    [0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, -5, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1],
])

R = np.array([
    [0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0],
])

O = np.array([
    [0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 1],
    [0, 1, 0, 0, 0, -1, 0],
])

x = 4
y = -2
v1 = x * x
v2 = v1 * v1         # x^4
v3 = -5*y * y
out = v3*v1 + v2    # -5y^2 * x^2

witness = np.array([1, out, x, y, v1, v2, v3])

print("Result: R1CS witness verification:", all(np.equal(np.matmul(L, witness) * np.matmul(R, witness), np.matmul(O, witness))))

## Finite Field Arithmetic

GF = galois.GF(79)

L = np.array([
    [0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 74, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1],
])

R = np.array([
    [0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0],
])

O = np.array([
    [0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 1],
    [0, 1, 0, 0, 0, 78, 0],
])


L_galois = GF(L)
R_galois = GF(R)
O_galois = GF(O)

x = GF(4)
y = GF(79-2) # we are using 79 as the field size, so 79 - 2 is -2
v1 = x * x
v2 = v1 * v1         # x^4
v3 = GF(79-5)*y * y
out = v3*v1 + v2    # -5y^2 * x^2

witness = GF(np.array([1, out, x, y, v1, v2, v3]))

print("Result: R1CS witness verification in GF:", all(np.equal(np.matmul(L_galois, witness) * np.matmul(R_galois, witness), np.matmul(O_galois, witness))))

## Polynomial interpolation in finite fields

def interpolate_column(col):
    xs = GF(np.array([1,2,3,4]))
    return galois.lagrange_poly(xs, col)

# axis 0 is the columns. apply_along_axis is the same as doing a for loop over the columns and collecting the results in an array
U_polys = np.apply_along_axis(interpolate_column, 0, L_galois)
V_polys = np.apply_along_axis(interpolate_column, 0, R_galois)
W_polys = np.apply_along_axis(interpolate_column, 0, O_galois)

print("Two first U polynomials are:", U_polys[:2])
print("Two first V polynomials are:",V_polys[:2])
print("First W polynomial is:",W_polys[:1])

print("The third U polynomial is:", U_polys[2])
print("The third U polynomial evaluated at x=1:", U_polys[2](1))
print("The third U polynomial evaluated at x=2:", U_polys[2](2))
print("The third U polynomial evaluated at x=3:", U_polys[2](3))
print("The third U polynomial evaluated at x=4:", U_polys[2](4))


## Computing h(x)

def inner_product_polynomials_with_witness(polys, witness):
    mul_ = lambda x, y: x * y
    sum_ = lambda x, y: x + y
    return ft.reduce(sum_, map(mul_, polys, witness))

term_1 = inner_product_polynomials_with_witness(U_polys, witness)
term_2 = inner_product_polynomials_with_witness(V_polys, witness)
term_3 = inner_product_polynomials_with_witness(W_polys, witness)

print("First QAP term:", term_1)
print("Second QAP term:", term_2)
print("Third QAP term:", term_3)

# t = (x - 1)(x - 2)(x - 3)(x - 4)
t = galois.Poly([1, 78], field = GF) * galois.Poly([1, 77], field = GF) * galois.Poly([1, 76], field = GF) * galois.Poly([1, 75], field = GF)

h = (term_1 * term_2 - term_3) // t

print("t(x) =", t)
print("h(x) =", h)

print("Does the division done to obtain h give a remainder?", not(term_1 * term_2 == term_3 + h * t))