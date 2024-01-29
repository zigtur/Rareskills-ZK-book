# Encrypted Polynomial Evaluation

We explained how to do homomorphic encryption for multiplication in [bilinear pairing](../bilinear-pairing/README.md).
How can we do homomorphic encryption for exponents?
As we are using polynomials, this is required.

The asymmetric pairing we were using in this bilinear pairing part isn't practical for exponents,
as it would require multiplying $G_{12}$ points.
We need a different strategy if we are going to deal with exponents larger than $2$.

## Encrypt the values with Elliptic curves
Let's take $39 = x^3 - 4x^2 +3x - 1$.
The answer is $x=5$.
What we do is encrypting the values of $x$, $x^2$ and $x^3$ and give them to the verifier.
Without modulo aspect, we get:
$$x_1 = g^{5^1} = g^5$$
$$x_2 = g^{5^2} = g^{25}$$
$$x_3 = g^{5^3} = g^{125}$$

The verifier will compute:
$$y = x_3 - 4x_2 + 3 x_1 -1$$
$$g^{39} = g^{125} \cdot 4g^{-25} \cdot 3 g^{5} \cdot g^{-1} (mod\ p)$$
 
As $g$ is known by the verifier, he can easily get $g^{39}$.
Thanks to group theory magic, we can use the group of elliptic curves instead of the group of $g^n (mod\ p)$.
Elliptic curves are more efficient.
The only change is scalar multiplication by the generator point instead of raising the generator integer to a power.

The [encrypted-evalution.py](./encrypted-evaluation.py) python script shows an encrypted evaluation of the example polynomial, using elliptic curves.

*Note: X, X2 and X3 are passed by the prover to the verifier.*


## Trusted Setup
In a trusted setup, a trusted third party (can be MPC) generate a secret value $\tau$ and encrypt it as:
$$\tau[G], \tau^2[G], \tau^3[G], ..., \tau^d[G]$$

The prover will plug this into their polynomial with coefficients $c_i$:
$$[result] = c_0[G] + c_1[\tau G] + c_2[\tau^2 G] + ... + c_d[\tau^d G]$$

*Note: $G$ is still the EC generator. $[$ and $]$ are used to show EC points.*

Neither the prover nor the verifier knows the input and output of this polynomial.
The verifier doesn't know the polynomial of the prover.
The fact that the prover doesn't know what point they are evaluating on and what the result is
becomes a tool **to prevent them from forging proofs**.
The fact that the input and output is encrypted helps prevent the verifier from learning the polynomial.

Note that $[result]$ is the same value as if we had evaluated the polynomial directly.
Say: $p(x) = c_0 + c_1 x + c_2 x^2 + ... + c_k x^d$, then evaluating this directly
on $\tau$ will give the same point:
$$p(\tau) = (c_0 + c_1 \tau + c_2 \tau^2 + ... + c_k \tau^d) [G] = c_0[G] + c_1 [\tau G] + c_2 [\tau^2 G] + ... + c_k [\tau^d G]$$

The important point here is that we can evaluate polynomials using elliptic curve points and get a valid output, but without knowing the point we evaluated the polynomial at.


## Implementation detail: polynomials over finite fields

As we are using Elliptic Curves, we can only evaluate polynomials
modulo "the order of the elliptic curve" (i.e. the number of points).

So, in our example, we need $39 = x^3 - 4x^2 +3x - 1 (mod\ n)$, with $n$ being the order of the EC group.

The [polynomial-on-ec.py](./polynomial-on-ec.py) python script shows how this can be achieved for our example polynomial.

The [polynomial-modulo.py](./polynomial-modulo.py) python script shows how this can be achieved for another example.

## Schwartz Zippel Lemma and encrypted polynomial evaluation
The Schwartz Zippel Lemma says that two unequal polynomials almost never overlap except at a number of points constrained by the degree.
In a big prime finite field, the degree is highly small compared to the order of the field.
So, if we evaluate two different polynomials at a random point $x$ and they evaluate to the same value,
then we can be almost perfectly certain that the two polynomials are the same.
This holds even *if we don't know the polynomials*.

We have now enough tool for a prover to prove to a verifier that they have four polynomials:
$A(x), B(x), C(x), D(x)$ such that $AB = CD$ and the verify can certify this fact without learning the polynomials.

The prover will use encrypted evaluation of all four polynomials to obtain $A,B,C,D$ and sends them to verifier.
The verifier can then verify the prover's claim that $AB = CD$.
As the prover doesn't know what point they are evaluating at, they can't architect polynomials that intersect at the point the third party setup chose.

If the verifier require the prover to use a known polynomial $D$, then it is not enough for him to learn $A, B, C$.
But it puts constraints on what the prover can use for $A, B, C$.

For example, one important feature is that the verifier now knows $AB$ has the same roots (and possible others)
as $D$ because when polynomials are multiplied by a non-zero polynomial,
the roots of the product polynomial is the union of the roots of the constituent polynomials.
Therefore, the roots of polynomial $D$ must be a subset of the roots of $AB$.


Another way to constrain the prover is to only supply them encrypted powers of $x$ up to a limiter power. This constrains the degree of polynomial $AB$.

A unknown polynomial of with a known upper bound on the degree and a known set of roots is not unique, but nonetheless “says something” and can be used to encode information with some clever transformations.
