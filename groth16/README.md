# Groth16

The Groth16 algorithm enables to compute a QAP over Elliptic Curve points derived in a trusted setup.
This can be quickly checked by a verifier.
It uses auxiliary EC points from the trusted setup to prevent forged proofs.

## Introduction
### Prerequisites
All previous chapters of the ZK book are required. See [summary](../README.md) for this.

### Notation
Given a R1CS $Ls \odot Rs = Os$, we refer the polynomial $u,v,w$ as:
$$u_i(x) = u_0(x), u_1(x), ..., u_m(x) = \phi(L)$$
$$v_i(x) = v_0(x), v_1(x), ..., v_m(x) = \phi(R)$$
$$w_i(x) = w_0(x), w_1(x), ..., w_m(x) = \phi(O)$$

$\phi$ is the transformation from R1CS to QAP. It interpolates the $m$ columns R1CS into $m$ polynomials. Among other, it uses Lagrange interpolation.

$p_{ij}$ will refer to the $j^{th}$ coefficient of the $i^{th}$ polynomial of the $p$ collection of polynomials.
$j=0$ refers to the constant portion of the polynomial, while $j=3$ corresponds to the coefficient attached to $x^3$.

Elliptic Curve points are written with square brackets with a subscript that indicates with EC group it belongs to, for example $[A]_1$ in fact corresponds to $[a G_1]$.
Groth16 isn't required to use the bilinear pairing described with $G_1, G_2, G_{12}$.
In practice, it is the most common EC family used with Groth16.

### Motivation
In the [QAP over Elliptic Curve](../qap-over-elliptic-curve/README.md) chapter,
we have seen that the prover could simply invent values $a,b,c$ such that $ab = c$
and present those as EC points to the verifier.

The verifier has no idea if the provided $[A]_1, [B]_2, [C]_1$ points were the result of a satisfied QAP or made up values.

To force the prover to be honest without too much computational efforts, a first algorithm has appeared: [**Pinocchio: Nearly Practical Verifiable Computation**](https://eprint.iacr.org/2013/279.pdf). ZCash based its first version on it.

Then, Groth16 was able to accomplish the same thing in much fewer steps.
This algorithm is still widely used today, as no algorithm since has produced as efficient verifier steps.
Other existing algorithms have notably eliminated the trusted setup, or highly reduced the amount of work of the prover.


## Prevent forgery - part 1: introducing $\alpha$ and $\beta$
### Secret shifting
The prover can fake values because he knows the values of $[A]_1, [B]_2, [C]_1$.
We add elliptic curve points to $[A]_1$ and $[B]_2$, respectively $[\alpha G_1] = [\alpha]$ and $[\beta G_2] = [\beta G_2]$:

$$[A]_1 = [A_{old}]_1 + [\alpha]_1$$

$$[B]_2 = [B_{old}]_2 + [\beta]_2$$

*Note: The prover knows the values $[A_{old}]_1 = [a_{old} G_1]_1$ and $[B_{old}]_2 = [b_{old} G_2]_2$

By doing this, the prover cannot predict the result of pairing $[A]_1$ and $[B]_2$,
because they don't have the new values $a$ and $b$ leading to $[A]_1 = [a G_1]_1$ and $[B]_2 = [b G_2]_2$.

The $\alpha$ and $\beta$ values are generated during the trusted setup, and **must be erased** once the corresponding EC points have been generated.
Only the EC points should be kept.

This shift in $A$ and $B$ still permits to create a balanced equation from the original QAP. First a recall of the QAP equation:

$$\sum\limits_{i=0}^{m} a_i u_i(x) \sum\limits_{i=0}^{m} a_i v_i(x) = \sum\limits_{i=0}^{m} a_i w_i(x) + h(x)t(x)$$

Now, we can add the $\alpha$ and $\beta$ values to it:

$$(\alpha + \sum\limits_{i=0}^{m} a_i u_i(x)) (\beta + \sum\limits_{i=0}^{m} a_i v_i(x))$$

$$= \alpha \beta + \beta \sum\limits_{i=0}^{m} a_i u_i(x) + \alpha \sum\limits_{i=0}^{m} a_i v_i(x) + \underbrace{\sum\limits_{i=0}^{m} a_i u_i(x) \sum\limits_{i=0}^{m} a_i v_i(x)}_{before\ substitution}$$

$$= \alpha \beta + \beta \sum\limits_{i=0}^{m} a_i u_i(x) + \alpha \sum\limits_{i=0}^{m} a_i v_i(x) + \underbrace{\sum\limits_{i=0}^{m} a_i w_i(x) +h(x)t(x)}_{after\ substitution}$$
$$\underbrace{(\alpha + \sum\limits_{i=0}^{m} a_i u_i(x))}_{A} \underbrace{(\beta + \sum\limits_{i=0}^{m} a_i v_i(x))}_{B} = \alpha \beta +  \underbrace{\sum\limits_{i=0}^{m} a_i (\beta u_i(x) + \alpha v_i(x) + w_i(x)) +h(x)t(x)}_{C}$$

We can see our $A$, $B$ and $C$ part. The $\alpha \beta$ is computed by the verifier.
The underlined sections are computed by the verifier.

In this section, we have seen how introducing shifts keep the QAP balanced.
Now, we are going to show how this prevents forgeries if $\alpha$ and $\beta$ are unknown.

The verifier formula is modified. It was $pairing([A]_1, [B]_2) == pairing([C]_1, [G_2]_2)$.
Now, the formula is $pairing([A]_1, [B]_2) == pairing([\alpha]_1, [\beta]_2) + pairing([C]_1, [G_2]_2)$.

Let's demonstrate that now, the prover can't invent $A, B$ and compute $C$ or invent $C$ and derive $A$ and $B$.

### Attack 1: Forging A, B and deriving C
Let's suppose the prover randomly select $a'$ and $b'$.
They have the EC points $[A']_1, [B']_2$.
They result in a pairing $[D]_{12}$.
The malicious prover has to compute $[D]_{12} - [[\alpha]_1 [\beta]_2]_{12} = [C']_{12}$.

Then, the $[C']_{12}$ is a $G_{12}$ point. But he needs a $G_1$ point.
The malicious prover would have to take the discrete logarithm of $[C']_{12}$ to get $c'$ and then multiply it with $G_1$ to get $[c' G_1]_1$.
But the discrete logarithm is infeasible. It is the DLP that allows the whole EC cryptography.
The reason the attack fails is because the attacker doesn't know $\alpha \beta$ value.

### Attack 2: Forging C and deriving A, B
Attakcer takes $c'$ and computes $[C']_1$.
They can try to discover a compatible $a', b'$ such that $a'b'=c'$.
He computes: $[D']_{12} = pairing([[\alpha]_1 [\beta]_2]) + pairing([C']_{1}, [G_2]_2)$.

Now, attacker needs to split $[D']_{12}$ into $[A]_1$ and $[B]_2$.
Here he runs into the DLP again because he doesn't know the preimages of $[D']_{12}$.
Given an elliptic curve point in $G_{12}$,
you cannot find two points from $G_{1}$ and $G_{2}$ that pair to it unless
you know the underlying field element that generated the $G_{12}$ element.


### Attack 3: Forging [A’] and [B’] with [a’G₁] + [α]₁ and [b’G₂] + [β]₂ and computing [C’]

Here are the steps for the attack:
1. Pick a random $a'$ and $b'$
2. Generate $[A'] = a'[G_1]_1 + [\alpha]_1$ and $[B'] = b'[G_2]_2 + [\beta]_2$
3. Then, we have $pairing([A']_1, [B']_2) == pairing([\alpha]_1, [\beta]_2) + pairing([C]_1, [G_2]_2)$
   1. As the [pairing-tests.py](./pairing-tests.py) python script shows, calculating $c'=a'b'$ doesn't make the job
   2. $pairing(([a'G_1]_1 + [\alpha]_1), ([b'G_2]_2 + [\beta]_2)) \neq pairing([\alpha]_1, [\beta]_2) + pairing([a'b' G_1]_1, [G_2]_2)$
4. $pairing(([a'G_1]_1 + [\alpha]_1), ([b'G_2]_2 + [\beta]_2)) - pairing([\alpha]_1, [\beta]_2) = pairing([C]_1, [G_2]_2)$ doesn't work neither


### Adjusting the trusted setup
Get back to the $C$ part of our QAP equation.

$$C = \sum\limits_{i=0}^{m} a_i (\beta u_i(x) + \alpha v_i(x) + w_i(x)) +h(x)t(x)$$

As $\beta$ will be an EC point after the trusted setup, it cannot be multiplied with the polynomial without doing a pairing.
That would cause $C$ to no longer be a $G_1$ point.

But, the terms $\beta u(\tau) + \alpha v(\tau) + w(\tau)$ can be precomputed at $\tau$ during the trusted setup.
The following is computed during setup:

$$\langle \beta u_0(\tau) + \alpha v_0(\tau) + w_0(\tau), \beta u_0(\tau) + \alpha v_0(\tau) + w_0(\tau), ..., \beta u_m(\tau) + \alpha v_m(\tau) + w_m(\tau) \rangle$$

*Note: here polynomials are simplified, $u_0(\tau) = u_{0,0}(\tau^0) + u_{0,1}(\tau^1) + ... + u_{0,n-1}(\tau^{n-1})$ and so on.*


### Recap: Computing a proof

We begin with a R1CS circuit turned into a QAP of form: $\sum\limits_{i=0}^{m} a_i u_i(x) \sum\limits_{i=0}^{m} a_i v_i(x) = \sum\limits_{i=0}^{m} a_i w_i(x) + h(x)t(x)$.
$m$ is the number of columns and $n$ is the number of rows.
Polynomials will have degree $n-1$, so we only need to compute powers of $\tau$ up to that power.

#### Trusted setup
During the trusted setup, the followings are computed:
- powers of $\tau$ for $A$:
  - $\underline{\{\tau^i[G_1]_1\}^{n-1}_{i=0}} = \{[G_1]_1, [\tau G_1]_1, [\tau^2 G_1]_1, ..., [\tau^{n-1} G_1]_1\}$
- random shift for $A$:
  - $\underline{[\alpha G_1]_1}$
- powers of $\tau$ for $B$:
  - $\underline{\{\tau^i[G_2]_2\}^{n-1}_{i=0}} = \{[G_2]_2, [\tau G_2]_2, [\tau^2 G_2]_2, ..., [\tau^{n-1} G_2]_2\}$
- random shift for $B$:
  - $\underline{[\beta G_2]_2}$
- powers of $\tau$ for $C$:
  - $\underline{\{(\beta u_i (\tau^i) + \alpha v_i (\tau^i) + w_i(\tau^i)) [G_1]_1 \}^{n-1}_{i=0}} = \{ (\beta u_0 (\tau^0) + \alpha v_0 (\tau^0) + w_0(\tau^0)) [G_1]_1, (\beta u_1 (\tau^1) + \alpha v_1 (\tau^1) + w_1(\tau^1)) [G_1]_1, ..., (\beta u_{n-1} (\tau^{n-1}) + \alpha v_{n-1} (\tau^{n-1}) + w_{n-1}(\tau^{n-1})) [G_1]_1 \}$
- powers of $\tau$ for $h(\tau)t(\tau)$:
  - $\underline{\{ \tau^i t(\tau) [G_1]_1 \}^{n-2}_{i=0}} = \{ \tau^0 t(\tau) [G_1]_1, \tau^1 t(\tau) [G_1]_1, ..., \tau^{n-2} t(\tau) [G_1]_1 \}$

All the underlined elements are made public.
The prover will use them.

#### Prover steps
The prover computes the followings:

$$[A]_1 = [\alpha]_1 + \sum\limits_{i=0}^{m} a_i [u_i(\tau)]_1$$

$$[B]_2 = [\beta]_2 + \sum\limits_{i=0}^{m} a_i [v_i(\tau)]_2$$

$$h(x) = \frac{\sum\limits_{i=0}^{m} a_i u_i(x) \sum\limits_{i=0}^{m} a_i v_i(x) - \sum\limits_{i=0}^{m} a_i w_i(x)}{t(x)}$$

$$[h(\tau)t(\tau)]_1 = \sum\limits_{i=0}^{deg(h)} h_i [\tau_i t(\tau) G_1]_1$$

$$[C]_1 = \sum\limits_{i=0}^{m} a_i [\beta u_i(\tau) + \alpha v_i (\tau) + w_i(\tau)]_1 + [h(\tau)t(\tau)]_1$$

$$proof = ([A]_1, [B]_2, [C]_1)$$

*Note: all EC points needed by the prover for its calculations have been precomputed during trusted setup.*

#### Verifier steps
The verifier only needs to compute $pairing([A]_1, [B]_2) == pairing([\alpha]_1, [\beta]_2) + pairing([C]_1, [G_2]_2)$.
If the equality holds, then verifier accepts the proof.

## Prevent forgery - part 2: separating public and private inputs with $\gamma$ and $\delta$
We split the QAP into the portions computed by the verifier (public inputs) and the prover (private inputs).

$$\sum\limits_{i=0}^{m} a_i w_i(x) = \underbrace{\sum\limits_{i=0}^{l} a_i w_i(x)}_{public\ inputs} + \underbrace{\sum\limits_{i=l+1}^{m} a_i w_i(x)}_{private\ inputs}$$

Here $l$ refers to the first $l$ elements of the witness vector which are public.
For example, with a witness vector $[1, out, X_1, x_2, ...]$, $l$ could be $1$.
So the first two elements would be public ($1$ and $out$).
$out$ is usually public.

The prover will adapt its $[C]_1$ calculations:

$$[C]_1 = \sum\limits_{i=l+1}^{m} a_i [\beta u_i(\tau) + \alpha v_i (\tau) + w_i(\tau)]_1 + [h(\tau)t(\tau)]_1$$

And the verifier will have to compute the public portion using the elliptic curve points from the trusted setup.
The verification formula changes a bit:

$$pairing([A]_1, [B]_2) == pairing([\alpha]_1, [\beta]_2) + pairing([C]_1, [G_2]_2) + pairing(\sum\limits_{i=0}^{l} a_i [\beta u_i(\tau) + \alpha v_i (\tau) + w_i(\tau)]_1, [G_2]_2)$$


### Preventing forgeries with public inputs
There is a possible attack on the public inputs parameters.
To avoid it, the trusted setup divides $w_0(\tau)$ and $w_1(\tau)$ by a secret variable $\gamma$
and the prover portion by a different variable $\delta$.
The corresponding EC points $[\gamma], [\delta]$ are made available so that the prover and the verifier can cancel them out.

#### Trusted setup with public inputs
Our trusted setup with public inputs is a little bit modified:
- powers of $\tau$ for $A$:
  - $\{\tau^i[G_1]_1\}^{n-1}_{i=0}$
- random shift for $A$:
  - $[\alpha G_1]_1$
- powers of $\tau$ for $B$:
  - $\{\tau^i[G_2]_2\}^{n-1}_{i=0}$
- random shift for $B$:
  - $[\beta G_2]_2$
- powers of $\tau$ for $public inputs$:
  - $\{\gamma^{-1} (\beta u_i (\tau^i) + \alpha v_i (\tau^i) + w_i(\tau^i)) [G_1]_1 \}^{l}_{i=0}$
- powers of $\tau$ for $private inputs$:
  - $\{\delta^{-1} (\beta u_i (\tau^i) + \alpha v_i (\tau^i) + w_i(\tau^i)) [G_1]_1 \}^{n-1}_{i=l+1}$
- powers of $\tau$ for $h(\tau)t(\tau)$:
  - $\{\delta^{-1} \tau^i t(\tau) [G_1]_1 \}^{n-2}_{i=0}$
- $\gamma$ and $\delta$:
  - $[\gamma G_2]_2, [\delta G_2]_2$

#### Verification step with $\gamma$ and $\delta$
Instead of pairing with $G_2$, we pair with $[\gamma]$ and $[\delta]$:

$$pairing([A]_1, [B]_2) == pairing([\alpha]_1, [\beta]_2) + pairing([C]_1, [\delta]_2) + pairing(\sum\limits_{i=0}^{l} a_i [\beta u_i(\tau) + \alpha v_i (\tau) + w_i(\tau)]_1, [\gamma]_2)$$

The $[\gamma]$ and $[\delta]$ will cancel out if the prover truly used the polynomials from the
trusted setup.
The prover and the verifier do not know the field element corresponding to those EC points,
so they cannot cause the terms to cancel out unless they use the values from the trusted setup.

If the prover uses polynomial evaluations from the public input portion of the witness, the $\gamma$ and $\delta$ terms will not cancel.

#### True Zero Knowledge: $r$ and $s$
Our scheme is not yet truly ZK.
If an attacker guess our witness vector (which can be possible if values used are predictable),
then they can verify their guess is correct by comparing their constructed proof to the original one.

To enforce true ZK, another random shift is added during the **proving phase** instead of the
trusted setup phase.
The prover samples two random field elements $r$ and $s$ and shifts their values accordingly:

$$[A]_1 = [\alpha]_1 + \sum\limits_{i=0}^{m} a_i [u_i(\tau)]_1 + r[\delta]_1$$

$$[B]_2 = [\beta]_2 + \sum\limits_{i=0}^{m} a_i [v_i(\tau)]_2 + s[\delta]_2$$

$$[B]_1 = [\beta]_1 + \sum\limits_{i=0}^{m} a_i [v_i(\tau)]_1 + s[\delta]_1$$

$$[C]_1 = \sum\limits_{i=0}^{m} a_i [\beta u_i(\tau) + \alpha v_i (\tau) + w_i(\tau)]_1 + [h(\tau)t(\tau)]_1 + s[A]_1 + r[B]_1 - rs[\delta]_1$$

*Note: This requires $[\beta]_1$ and $[\delta]_1$ to be produced during the trusted setup.*

**EXERCISE: Explains why adding $r$ and $s$ doesn't alter the equation balance for the verifier.
To make it easier, consider setting $\alpha = \beta = 0$ and $\gamma = \delta = 1$.


## Conclusion
Now that we have been through all the explanations, we can look at the [Groth16 paper](https://eprint.iacr.org/2016/260.pdf)
to get the official algorithm.

Here are some minor notation differences:
- the paper uses $x$ notation, we used $\tau$.
- the paper's notation of $\tau$ is a collection of variables which can be ignored.
- encrypted evaluations are implicit in the paper.
- the paper writes $\gamma$ and $\delta$ as division instead of inverse, which is the same in a finite field.
- the paper uses $[A]_1 \cdot [B]_2$ for pairing.
- the paper uses $\pi$ as the proof, we used $([A]_1, [B]_2, [C]_1)$.
- the paper uses $\sigma_1$ to refers to the $G_1$ points collection from the trusted setup. $\sigma_2$ for $G_2$ point collection.


### Go further

Here are some interesting additional ressources:
- Groth16 on Solana: https://lib.rs/crates/groth16-solana
- Tornado cash's proof verification code: https://github.com/tornadocash/tornado-core/blob/master/contracts/Verifier.sol#L192