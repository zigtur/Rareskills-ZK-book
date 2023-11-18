# R1CS to QAP over a finite field in Python
*The [r1cs-to-qap.py](./r1cs-to-qap.py) python script shows the example code.*

Let's encode: $out = x^4 - 5y^2 x^2$.

This can be break down as the following constraints:
$$v1 = x * x$$
$$v2 = v1 * v1$$
$$v3 = -5y * y$$
$$-v2 + out = v3 * v1$$

We need to pick a prime field we will do this over.
When combining with elliptic curve, the order of our prime field needs to equal
the order of the elliptic curve.

For this example, we will pick number $79$. 

## R1CS
*The [r1cs-part.py](./r1cs-part.py) python script shows the code of this section.*

We break our constraints into $L, R, O$ matrices.
The solution vector $s$ (also called witness) is $s = [1, out, x, y, v1, v2, v3]$.

In Python,those three matrices will be:
```python
import numpy as np

# 1, out, x, y, v1, v2, v3
L = np.array([
    [0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, -5, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1],
])

R = np.array([
    [0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0],
])

O = np.array([
    [0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 1],
    [0, 1, 0, 0, 0, -1, 0],
])
```

The constructed R1CS can easily be verifier using a valid witness and do the matrix multiplication:
```python
x = 4
y = -2
v1 = x * x
v2 = v1 * v1         # x^4
v3 = -5*y * y
out = v3*v1 + v2    # -5y^2 * x^2

witness = np.array([1, out, x, y, v1, v2, v3])

assert all(np.equal(np.matmul(L, witness) * np.matmul(R, witness), np.matmul(O, witness))), "not equal"
```

## Finite Field Arithmetic
*The [r1cs-galois.py](./r1cs-galois.py) python script shows the code of this section.*

In Python, there is the `galois` library to do modular arithmetic.
A quick tutorial of this library is available in [galois-tuto.py](./galois-tuto.py).

Our galois field does not support negative values. In our R1CS, we will then need to modify the negative values. For example, $-1 (mod\ 79) = 78$.
We could easily automate it in Python.
We will do it by hand for now.

So, we can construct the following R1CS matrices:
```python
L = np.array([
    [0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 74, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1],
])

R = np.array([
    [0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0],
])

O = np.array([
    [0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 1],
    [0, 1, 0, 0, 0, 78, 0],
])
```

Converting them to galois field arrays can be done with `GF`.
Our witness also needs to be recomputed as it contains negative values.
```python
L_galois = GF(L)
R_galois = GF(R)
O_galois = GF(O)

x = GF(4)
y = GF(79-2) # we are using 79 as the field size, so 79 - 2 is -2
v1 = x * x
v2 = v1 * v1         # x^4
v3 = GF(79-5)*y * y
out = v3*v1 + v2    # -5y^2 * x^2

witness = GF(np.array([1, out, x, y, v1, v2, v3]))

print("Result: R1CS witness verification in GF:", all(np.equal(np.matmul(L_galois, witness) * np.matmul(R_galois, witness), np.matmul(O_galois, witness))))
```

## Polynomial interpolation in finite fields
*The [r1cs-galois.py](./r1cs-galois.py) python script shows the code of this section.*

Now, we need to turn each of the columns of the matrices into a list of galois polynomials.
As we have 4 constraints, matrices have 4 rows, so we will interpolate $x=[1,2,3,4]$.
To interpolate each columns, we can create a python function that will use lagrange interpolation over a column.
Then, we just use this function for each column and we collect all the polynomials.
```python
def interpolate_column(col):
    xs = GF(np.array([1,2,3,4]))
    return galois.lagrange_poly(xs, col)

# axis 0 is the columns. apply_along_axis is the same as doing a for loop over the columns and collecting the results in an array
U_polys = np.apply_along_axis(interpolate_column, 0, L_galois)
V_polys = np.apply_along_axis(interpolate_column, 0, R_galois)
W_polys = np.apply_along_axis(interpolate_column, 0, O_galois)
```

An informal verification is to look at the result polynomial of all zero columns.
For example, the first column of the matrix $L$ contains all zeros.
So, the interpolated polynomial should be zero.
It should be the case for all zero columns
```python
print(U_polys[:2])
print(V_polys[:2])
print(W_polys[:1])
```

We can also evaluate other interpolated polynomial.
For example, the polynomial interpolated from the third column of $L$ should give $1$ if $x=1$, $0$ if $x=[2,3,4]$.
The following python code evaluates this polynomial:
```python
print("The third U polynomial is:", U_polys[2])
print("The third U polynomial evaluated at x=1:", U_polys[2](1))
print("The third U polynomial evaluated at x=2:", U_polys[2](2))
print("The third U polynomial evaluated at x=3:", U_polys[2](3))
print("The third U polynomial evaluated at x=4:", U_polys[2](4))
```

All the interpolated polynomials could be evaluated at $x=[1,2,3,4]$ following our previous method.

## Computing h(x)
Reminder: This is the formula for a [Quadratic Arithmetic Program](../quadratic-arithmetic-programs/README.md):
$$\sum\limits_{i=0}^{m} a_i u_i(x) \sum\limits_{i=0}^{m} a_i v_i(x) = \sum\limits_{i=0}^{m} a_i w_i(x) + h(x)t(x)$$
Here, we can see three sums. Those will be called *terms* in the following section.

As there are 4 constrants, 4 rows in our R1CS, we know that $t(x) = (x-1)(x-2)(x-3)(x-4)$.
As the formula shows, each interpolated polynomial encodes one specific value of the witness vector.
This is achieved by multiplying the polynomial and the specific witness value.
Then, the final term is the sum of all those multiplications.

To compute the summation of each term, we can use the following piece of code:
```python
import functools as ft
def inner_product_polynomials_with_witness(polys, witness):
    mul_ = lambda x, y: x * y
    sum_ = lambda x, y: x + y
    return ft.reduce(sum_, map(mul_, polys, witness))

term_1 = inner_product_polynomials_with_witness(U_polys, witness)
term_2 = inner_product_polynomials_with_witness(V_polys, witness)
term_3 = inner_product_polynomials_with_witness(W_polys, witness)
```

Once the three terms have been calculated, it is possible to deduce the $h(x)$ term.
This polynomial can't be calculated unless we have a valid witness,
as the witness has already been combined with the polynomials.
The following code computes $h(x)$.


