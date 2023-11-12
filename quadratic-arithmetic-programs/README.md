# QAP - Quadratic Arithmetic Programs

A QAP is a system of equations chere the coefficients are monovariate polynomials and a valid
solution results in a single polynomial equality.
They are quadratic because they have exactly one polynomial multiplication.
QAP allow zk-SNARKs to be succint!

An R1CS evaluation is not succint due to many matrix multiplications.

Due to Schwartz-Zippel Lemma, polynomials allow us to make statements succinct.
In a sense, we can compress a polynomial down to a single point.
Key idea is:
1. Operations in R1CS form an algebraic ring
2. Polynomials under addition and multiplication are rings
3. There exists an easily computable homomorphism from R1CS to polynomials


Once we have a monovariate polynomial statement with only one polynomial equality, we can evaluate it succinctly.


## Schartz-Zippel Lemma
If two polynomials are randomly evaluated at a same $x$ value, and their value $y$ is the same, then one can be nearly certain that they are the same polynomial.

$\tau$ random, if $P_1(\tau) == P_2(\tau)$ then $P1 == P2$. This is what make the succinctness. Comparing coefficients of poly would be far less efficient.

We already how to make the R1CS evaluation ZK (see [Zero Knowledge Proofs with Rank 1 Constraint Systems](../zkp-with-r1cs/README.md)). We need to make it succinct.

Let's say I have a $poly$ transformation, and a $\tau$ random value.
- $u=poly(Ls)(\tau)$
- $v=poly(Rs)(\tau)$
- $w=poly(Os)(\tau)$

By SZ-LM, if $uv = w$, the polynomials are the same, then $Ls \odot Rs = Os$.

Better, we turn $u$, $v$, and $w$ into $[U],[V],[W]$ EC points to hide their values. Verifier pairs $[U]$ and $[V]$ and compares result to $[W]$, so we have ZK.

## Transform R1CS into a single polynomial
### Recalls
We need to know:
- Rings (see [ring section](../rings-and-fields/README.md))

### Rings
R1CS is a ring, as it has:
- operator: addition
- identity: all vector zero
- inverse: vector with elements multiplied by -1
- operator: multiplication (hadamard product)
- inverse: no inverse for multiplication


Polynomials are also a ring, it has:
- operator: addition
- identity: zero polynomial $(0x^0)$
- inverse: polynomial with coefficients of opposite sign
- operator: multiplication
- inverse: no inverse for multiplication

### Ring homomorphism
Theorem: There exists a ring homomorphism from columns vectors of dimension $n$ with real numbers elements to polynomials with real coefficients.

### Polynomials
We need to think polynomial as an infinite set of pairs (x,y) instead of $a = ax^2 + bx + c$.

If we want to add two polynomials, we need to define the relation that combines those two sets of pairs: cartestian product.

