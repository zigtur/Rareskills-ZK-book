from py_ecc.bn128 import G1, G2, pairing, add, multiply, eq


## Introduction
print("----------------------\nIntroduction\n----------------------")

print(G1)
print(G2)

print("G1 + G1 == G1 * 2:", eq(add(G1, G1), multiply(G1, 2)))
print("G2 + G2 == G2 * 2:",eq(add(G2, G2), multiply(G2, 2)))

try:
    add(G1, G2)
except:
    print("Addition with elements in different group doesn't work")

print("G1 + G1 + G1 = G1 * 3:", eq(add(add(G1, G1), G1), multiply(G1, 3)))


## Pairing
print("\n----------------------\nPairing\n----------------------")

A = multiply(G2, 5)
B = multiply(G1, 6)
print(pairing(A, B))

C = multiply(G2, 5 * 6)

### e(P,Q) = e(R, 1)
pairing(A, B) == pairing(C, G1)

print("e(5*G2, 6*G1) == e(5*6*G2, G1): ", pairing(A, B) == pairing(C, G1))


