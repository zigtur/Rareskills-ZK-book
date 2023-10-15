from py_ecc.bn128 import G1, multiply, add

# Prover
secret_x = 7

x = multiply(G1, 7)
var23 = 23

proof = (x, var23, 161)

# verifier
if multiply(G1, proof[2]) == multiply(proof[0], proof[1]):
    print("statement is true")
else:
    print("statement is false")