from py_ecc.bn128 import G1, G2, pairing, add, multiply, eq

## Pairing test
print("\n----------------------\nPairing tests\n----------------------")


alpha = multiply(G1, 23)
beta = multiply(G2, 512)

A = multiply(G1, 5)
B = multiply(G2, 6)

A_p = add(A, alpha)
B_p = add(B, beta)



C = multiply(G1, 5 * 6)

print("pairing(A', B') = ", pairing(B_p, A_p))
print("pairing(alpha, beta) + pairing(G2, C) =", pairing(beta, alpha) + pairing(G2, C))

print("pairing(A', B') - pairing(alpha, beta) =", pairing(B_p, A_p) - pairing(beta, alpha))
### e(P,Q) = e(R, 1)
print("Two pairings are equal?", pairing(B_p, A_p) == pairing(beta, alpha) + pairing(G2, C))
print("Two pairings are equal?", pairing(B_p, A_p) -  pairing(beta, alpha) == pairing(G2, C))
