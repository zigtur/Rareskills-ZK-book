# Zero Knowledge Proofs with Rank 1 Constraint Systems

Given a R1CS circuit, it is possible to create a ZK Proof of having a witness.

## R1CS
R1CS was explained in [Rank-1 Constraint Systems](../rank-1-constraint-systems/README.md) section.

The main point is that we produce a $\vec{w}$ vector, also called $s$.
It contains all inputs, outputs and intermediates values of the circuit.

The notation can be $C \vec{w} = A \vec{w} * B \vec{w}$ or $Ls \odot Rs = Os$.

## ZK proof algorithm for an R1CS

We can "encrypt" the witness vector, in such a way that the math still works properly in the R1CS.

To do this, we will use elliptic curves.

### Goal
*Note: Mathematical expressions here can be wrong!*

Recall the [bilinear pairing](../bilinear-pairing/README.md) section, we are trying to create 3 vectors derived from the solution one $\vec{w}$.
$$\vec{w_1} = \vec{w} * G_1$$
$$\vec{w_2} = \vec{w} * G_2$$
$$\vec{w_{12}} = \vec{w} * G_{12}$$

Then the final idea is to get:
$$ A \vec{w_1} * B \vec{w_2} = C \vec{w_{12}}$$


### Prover steps

The prover will have to encrypt is $s$ vector (solution) also name $\vec{w}$.
All entries will be encrypted by multiplying with the $G_1$ point.

If $s = [1, out, x, y]$, then the produced $s_1$ vector is $\vec{w_1} = s_1 = [G_1, out G_1, x G_1, y G_1]$. The same applies for $\vec{w_2} = s_2 = [G_2, out G_2, x G_2, y G_2]$ and $\vec{w_{12}} = s_{12}$.

In practice, $\vec{w_{12}} = \vec{w_{1}} * G_2$ because $G_{12}$ points are really big.



### Verifier steps

Then, for each row in the $A,B,C$ matrices, the following should hold:
$pairing(A \vec{w_1}, B \vec{w_2}) == pairing(C \vec{w_1}, G_2)$

The above pairing will be equal if and only if the proved has provided a valid witness $w$.


### Public inputs

The public inputs are simply not encrypted before being sent to the verifier.

### Dealing with a malicious prover

```
Because the vectors are encrypted, the verifier cannot immediately know if the vector of G₁ points encrypts the same values as the vector of G₂ points.


However, the verifier can check for their equality with some extra steps.


This is left as an exercise for the reader.
```

The verifier can quickly verify that $\vec{w_1}$ corresponds to $\vec{w_2}$ by using bilinear pairing.

If $pairing(\vec{w_1}, G_2) == pairing(\vec{w_2}, G_1)$, then the verifier can be sure that the same witness $w$ have been used in both encrypted vectors.


## Conclusion

The work we have done here is not truly ZK. An attacker could try to guess the witness and then can easily verify the results.

This will be covered in Groth-16 course.