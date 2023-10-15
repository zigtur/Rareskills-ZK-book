# Elliptic curves over finite fields
*Note: for code examples, install **py_ecc** library.*

In cryptography, elliptic curves are used over a finite field. 


$5 + 7 (mod\ p)$ is homomorphic to $5G + 7G$ with $G$ the generator of the elliptic curve cyclic group.



## bn128 EC

**bn128** curve is used by Ethereum precompiles to verify ZK proofs. Its specs are:
```
field_modulus = 21888242871839275222246405745257275088696311157297823662689037894645226208583
y² = x³ + 3 (mod field_modulus)
```




### Code examples
- [Addition](./bn128-addition.py)
- [Homomorphism](./bn128-curveorder.py)
- [Inverse](./bn128-inverse.py)

## Basic ZK Proofs with Elliptic Curves
- Claim: “I know two values x and y such that x + y = 15”
- Proof: I multiply x by G1 and y by G1 and give those to you as A and B.
- Verifier: You multiply 15 by G1 and check that A + B == 15G1.

The [Basic ZK Proof code example](./bn128-basicZk.py) is available.

### Exercices
#### Ex1
Can you prove you know x such that 23x = 161? 

The [solution code is available](./bn128-ex1.py).

#### Ex2
Can you generalize this to more variables?

The [solution code is available](./bn128-ex2.py).


