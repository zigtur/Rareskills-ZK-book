from py_ecc.bn128 import G1, multiply, add

## Prove 25*x + x+y = 112

# Prover
secret_x = 4
secret_y = 8

x = multiply(G1, secret_x)
var25 = 25
y = multiply(G1, secret_y)

proof = (x, var25, y, 112)

# verifier
if multiply(G1, proof[3]) == add(multiply(proof[0], proof[1]), add( proof[0], proof[2])):
    print("statement is true")
else:
    print("statement is false")