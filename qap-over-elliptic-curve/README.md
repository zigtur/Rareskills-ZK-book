# QAP over Elliptic curves

We are going to explain how [encrypted evaluation](../encrypted-polynomial-evaluation/README.md) of a [Quadratic Arithmetic Program](../quadratic-arithmetic-programs/README.md) can be done.

## Recalls
This is the formula for a [Quadratic Arithmetic Program](../quadratic-arithmetic-programs/README.md):
$$\sum\limits_{i=0}^{m} a_i u_i(x) \sum\limits_{i=0}^{m} a_i v_i(x) = \sum\limits_{i=0}^{m} a_i w_i(x) + h(x)t(x)$$

This was derived from a [Rank 1 Constraint System](../rank-1-constraint-systems/README.md).
$u_i(x), v_i(x), w_i(x)$ are polynomials interpolated from the R1CS matrices $L, R, O$.
Those correspond to the left, right and output wires of the arithmetic circuit.
$a_i$ are the witness elements, part of the witness vector $s$.

## Concrete example
Let's take matrices $L, R, O$ with 4 rows and 3 columns.
Our interpolating polynomials will be of degree 3 ($number\ of\ rows - 1$).
As we have 3 columns, each matrix will produce 3 polynomials.
In total, 9 polynomials will be interpolated.

When transformed to QAP, we can represent the polynomials coefficients as follow:
$$u_1, u_2, u_3 = [\langle u_{1,0}, u_{1,1}, u_{1,2}, u_{1,3} \rangle, \langle u_{2,0}, u_{2,1}, u_{2,2}, u_{2,3} \rangle, \langle u_{3,0}, u_{3,1}, u_{3,2}, u_{3,3} \rangle]$$
$$v_1, v_2, v_3 = [\langle v_{1,0}, v_{1,1}, v_{1,2}, v_{1,3} \rangle, \langle v_{2,0}, v_{2,1}, v_{2,2}, v_{2,3} \rangle, \langle v_{3,0}, v_{3,1}, v_{3,2}, v_{3,3} \rangle]$$
$$w_1, w_2, w_3 = [\langle w_{1,0}, w_{1,1}, w_{1,2}, w_{1,3} \rangle, \langle w_{2,0}, w_{2,1}, w_{2,2}, w_{2,3} \rangle, \langle w_{3,0}, w_{3,1}, w_{3,2}, w_{3,3} \rangle]$$

To explain the notation, $u_{1,2}$ represents the coefficient of the first interpolated polynomial attached to $x^2$. The first interpolated polynomial represents the first column of the R1CS.
So $u_2(x) = u_{2,0} + u_{2,1} x + u_{2,2} x^2 + u_{2,3} x^3$.

The prover wishes to evaluate the QAP at point $\tau$:
$$\sum\limits_{i=0}^{m} a_i u_i(\tau) \sum\limits_{i=0}^{m} a_i v_i(\tau) = \sum\limits_{i=0}^{m} a_i w_i(\tau) + h(\tau)t(\tau)$$

$\tau$ is chosen randomly at the trusted setup.
It allows the verifier to test polynomial equality at that point.


## Trusted Setup

The trusted setup is need to do encrypted evaluation of the polynomial.
To create the trusted setup, pick a random value $\tau$ and for the generators $G_1$ and $G_2$ (two EC curves) do:
$$\langle [\tau^0 G_1], [\tau^1 G_1], [\tau^2 G_1], [\tau^3 G_1] \rangle$$
$$\langle [\tau^0 G_2], [\tau^1 G_2], [\tau^2 G_2], [\tau^3 G_2] \rangle$$

The first points will belong to the first elliptic curve group.
Thanks to the Discrete Logarithm Problem (DLP), $\tau$ is inextractible from those points.

## Evaluation of $u_i(\tau), v_i(\tau), w_i(\tau)$
The nine interpolated polynomials $u_i(\tau), v_i(\tau), w_i(\tau)$ can be evaluated by taking the elliptic curve points produced by the trusted setup.
Since we are doing an encrypted evaluation, the output is also encrypted.
For example:
$$[u_1(\tau)] = \langle u_{1,0}, u_{1,1}, u_{1,2}, u_{1,3} \rangle \cdot \langle [\tau^0 G_1], [\tau^1 G_1], [\tau^2 G_1], [\tau^3 G_1] \rangle$$
$$[u_1(\tau)] =  u_{1,0}[\tau^0 G_1] + u_{1,1} [\tau^1 G_1] + u_{1,2} [\tau^2 G_1] + u_{1,3} [\tau^3 G_1]$$
$$[u_1(\tau)] = \sum\limits_{j=0}^{3} u_{1, j} [\tau^j G_1]$$

This last result can be generalized to all the interpolated polynomials:
$$[u_i(\tau)] = \sum\limits_{j=0}^{3} u_{i, j} [\tau^j G_1]$$
$$[v_i(\tau)] = \sum\limits_{j=0}^{3} v_{i, j} [\tau^j G_2]$$
$$[w_i(\tau)] = \sum\limits_{j=0}^{3} w_{i, j} [\tau^j G_1]$$

*Note: $v_i$ is plugged to the second elliptic curve group (see $G_2$).*

Now we know how to evaluate those points.
Then we can compute:
$$\sum\limits_{i=0}^{m} a_i [u_i(\tau)]_1 \sum\limits_{i=0}^{m} a_i [v_i(\tau)]_2 = \sum\limits_{i=0}^{m} a_i [w_i(\tau)]_1 + [h(\tau)t(\tau)]_1$$

*Note: The notation $[]_x$ allows to show to which EC group the EC point belongs. Here it belongs to the EC group $x$.*

## Evaluating $h(\tau)t(\tau)$
The polynomial $t(x)$ is determined by the circuit.
In our case, it is $t(x) = (x-1)(x-2)(x-3)$.

$h(x)$ is then computed by the prover via the following equation:
$$h(x) = \frac{\sum\limits_{i=0}^{m} a_i u_i(x) \sum\limits_{i=0}^{m} a_i v_i(x) - \sum\limits_{i=0}^{m} a_i w_i(x)}{t(x)}$$

The prover actually realizes this operation.
This is expensive, it is one of the primary reason zk-SNARKs take a lot of time to prove.
The division will have no remainder if and only if the polynomials in the numerator truly interpolates $(1,0), (2,0), (3,0)$.
This is homomorphic to our R1CS having a valid solution: $Ls \odot Rs = Os$.

### Encrypted evaluation of $h$ and $t$
An encrypted evaluation results in an EC point.
This would force us to introduce a pairing to evaluate the multiplication of $h(\tau)$ and $t(\tau)$.
To avoid this, something can be done in the trusted setup phase.

$t(x)$ is known at trusted setup phase.
We know that is has a power of 3 (definition of the circuit).
During trusted setup, the setup agent can do:
$\langle [\tau^0 t(\tau) G_1], [\tau^1 t(\tau) G_1], [\tau^2 t(\tau) G_1], [\tau^3 t(\tau) G_1] \rangle$.

Then, we can simply take the inner product of the coefficients of $h(x)$ with those elements:
$$h(\tau)t(\tau) = \langle h_0, h_1, ... \rangle \cdot \langle [\tau^0 t(\tau) G_1], [\tau^1 t(\tau) G_1], [\tau^2 t(\tau) G_1], [\tau^3 t(\tau) G_1] \rangle$$
$$h(\tau)t(\tau) = \sum\limits_{i=0}^{deg(h)} h_i [\tau^i t(\tau) G_1]$$

This can be done because $h(\tau) t(\tau) = ht(\tau) = (h(x) * t(\tau))(\tau)$.
It feels strange.
The [example-ht-evaluation.py](./example-ht-evaluation.py) python script shows an example of this relation.

## Final evaluation
Given a circuit transformed to QAP defined with polynomials $u(x), v(x), w(x)$
and polynomial $t(x)$, and given a trusted setup:
$$\langle [\tau^0 G_1], [\tau^1 G_1], [\tau^2 G_1], [\tau^3 G_1] \rangle$$
$$\langle [\tau^0 G_2], [\tau^1 G_2], [\tau^2 G_2], [\tau^3 G_2] \rangle$$
$$\langle [\tau^0 t(\tau) G_1], [\tau^1 t(\tau) G_1], [\tau^2 t(\tau) G_1], [\tau^3 t(\tau) G_1] \rangle$$

The prover computes three elliptic curve points $[A]_1, [B]_2, [C]_1$ such that:
$$[A]_1 = \sum\limits_{i=0}^{m} a_i [u_i(\tau)]_1 = \sum\limits_{i=0}^{m} a_i \sum\limits_{j=0}^{n} u_{i,j}[\tau^j G_1]_1$$
$$[B]_2 = \sum\limits_{i=0}^{m} a_i [v_i(\tau)]_1 = \sum\limits_{i=0}^{m} a_i \sum\limits_{j=0}^{n} v_{i,j}[\tau^j G_2]_2$$
$$[C]_1 = \sum\limits_{i=0}^{m} a_i [w_i(\tau)]_1 + [h(\tau) t(\tau)]_1 = \sum\limits_{i=0}^{m} a_i \sum\limits_{j=0}^{n} w_{i,j}[\tau^j G_1]_1 + \sum\limits_{i=0}^{deg(h)} h_i [\tau^i t(\tau)G_1]_1$$

Finally, the verifier just compute $pairing([A]_1, [B]_2) == pairing([C]_1, [G_2]_2)$.
If the equality is true, the verifier accept the statement.

## Conclusion
Here we have a fully functional and succinct zero knowledge proof.
But, we have no idea if the prover really derived $[A]_1, [B]_2, [C]_1$ from the trusted setup using the QAP.
We don't also have a way to add public inputs.
We have a proof that the prover has a valid witness with none of the elements being public.

