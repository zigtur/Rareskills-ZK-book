from py_ecc.bn128 import neg, multiply, G1, G2
a = 4
b = 3
c = 6
d = 2
# negate G1 * a to make the equation sum up to 0
print("ZK Goal: Verify that: a * b == c * d\n------------------------")

print("-a G1: ",neg(multiply(G1, a)))

print("b G2: ",multiply(G2, b))

print("c G1: ",multiply(G1, c))

print("d G2: ",multiply(G2, d))



