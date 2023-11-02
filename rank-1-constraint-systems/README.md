# Rank-1 Constraint Systems


## Witness vector
The witness vector is a $1 \times n$ vector containing all the input, intermediate and output variables. It shows the execution values from start to finish.

By convention, the first element is always $1$.


### Example
Let's take the polynomial $out = x^2 y$
that we claim to know the solution for.
We must know $x$, $y$ and $out$.

R1CS requires one multiplication per constraint.
Our example must be written as:
$$v_1 = x * x$$
$$out = v_1 * y$$

Our witness vector would be: $[1, out, x, y, v_1]$.

For example, $[1, 18, 3, 2, 9]$ is a valid witness vector.
It satisfies:
$$9 = 3*3$$
$$18 = 9*2$$

## Example 1: Transforming out = x * y
The main goal is to produce a list of formulas that contain exactly one multiplication per formula.
It will have the form: $C_w = A_w * B_w$.

Matrix $A$ encode the "left hand side". Matrix "B" encode the "right hand side$. $C$ encodes the result variables.

$A, B, C$ are matrices with the same number of columns as the witness. Each column represents the same variable the index is using.

Witness has 4 elements, each of our matrices will have 4 columns. The number of rows corresponds to the number of constraints in the circuit. 1 row in our case.

$$C \vec{w} = A \vec{w} * B \vec{w}$$
$$\vec{w} = $$