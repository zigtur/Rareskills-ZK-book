# RareSkills - ZK-book


This repository contains my work on the [RareSkills ZK-book](https://www.rareskills.io/zk-book).

## Table of Contents

Chapter 1: [Set Theory](./set-theory/README.md)

Chapter 2: [Group Theory](./group-theory/README.md)

Chapter 3: [Rings and Fields](./rings-and-fields/README.md)

Chapter 4: [Elliptic Curve Addition](./elliptic-curve-addition/README.md)

Chapter 5: [Elliptic Curves in Finite Fields](./elliptic-curve-finite-field/README.md)

Chapter 6: [Bilinear Pairings](./bilinear-pairing/README.md)

Chapter 7: [Arithmetic Circuits](./arithmetic-circuits/README.md)

Chapter 8: [Rank 1 Constraint Systems]()

Chapter 9: [Zero Knowledge Proofs with Rank 1 Constraint Systems]()

Chapter 10: [Quadratic Arithmetic Programs]()

Chapter 11: [R1CS to QAP in Python]()

Chapter 12: [Encrypted Polynomial Evaluation]()

Chapter 13: [Quadratic Arithmetic Programs over Elliptic Curves]()

Chapter 14: [Groth16 Explained]()

Chapter 15: [Circom and Circomlib]()


## Summary
### Monoid
- A magma is a set with a closed binary operator.
- A semigroup is a magma where the binary operator must be associative.
- A monoid is a semigroup with an identity element.

### Group
It is a set with:
* an associative and closed binary operator
* an identity element
* every element has an inverse
* (abelian group:) 
    * binary operator is commutative

Order of a group = the number of elements in it

Cyclic group = group that has a generator element, allows to generate every other elements with the binary operator

Product of groups exist and are useful.

### Ring
It is a set with two binary operators such that:
- under first binary operator, the set is an abelian group
- under second binary operator, the set is a monoid
    - Monoid: only the inverse property is missing to make it a group
    - if monoid is commutative, then it is an **abelian ring**
- second binary distributes over the first


### Field
It is a set with two bin operators such that:
- under the first, the set is an abelian group
- under the second (excluding the zero element), the set is an abelian group


