from py_ecc.bn128 import G1, multiply, add, curve_order, eq, Z1
from functools import reduce
import galois

print("initializing a large field, this may take a while...")
GF = galois.GF(curve_order)

def inner_product(ec_points, coeffs):
    return reduce(add, (multiply(point, int(coeff)) for point, coeff in zip(ec_points, coeffs)), Z1)

def generate_powers_of_tau(tau, degree):
    return [multiply(G1, int(tau ** i)) for i in range(degree + 1)]

# p = x^3 - 4x^2 +3x - 1
p = galois.Poly([1, -4, 3, -1], field = GF)

# evaluate at 125 (no matter)
tau = GF(125)

# Trusted Setup
print("Trusted Setup: Generation of the powers of tau!")
powers_of_tau = generate_powers_of_tau(tau, p.degree)

# Here we are evaluating the polynomial and then bringing it to EC
print("Evaluating Polynomial BEFORE bringing it to elliptic curves (not done in practice)")
evaluate_then_convert_to_ec = multiply(G1, int(p(tau)))

# evaluate via encrypted evaluation# coefficients need to be reversed to match the powers
print("Evaluating directly on elliptic curves (done in practice)")
evaluate_on_ec = inner_product(powers_of_tau, p.coeffs[::-1])

if eq(evaluate_then_convert_to_ec, evaluate_on_ec):
    print("Final Result: The two Elliptic Curve points are equal!!!")