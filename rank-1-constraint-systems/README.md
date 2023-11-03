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

## Math and Python Examples

### Example 1: Transforming out = x * y
The main goal is to produce a list of formulas that contain exactly one multiplication per formula.
It will have the form: $C_w = A_w * B_w$.

Matrix $A$ encode the "left hand side". Matrix "B" encode the "right hand side$. $C$ encodes the result variables.

$A, B, C$ are matrices with the same number of columns as the witness. Each column represents the same variable the index is using.

Witness has 4 elements, each of our matrices will have 4 columns. The number of rows corresponds to the number of constraints in the circuit. 1 row in our case.

$$C \vec{w} = A \vec{w} * B \vec{w}$$
$$\vec{w} = [1, 4223, 41, 103]$$
$$A = [0, 0, 1, 0]$$
$$B = [0, 0, 0, 1]$$
$$C = [0, 1, 0, 0]$$


A [Python script](./r1cs-ex1.py) is available for this example.

### Example 2: Transforming out = x * y * z * u
R1CS requires one multiplication per constraint.
Our example must be written as:
$$v_1 = x * y$$
$$v_2 = v_1 * z$$
$$out = v_2 * u$$

Our witness vector will have 8 elements: $[1, out, x, y, z, u, v_1, v_2]$.
So, our $A,B,C$ matrices will have 8 columns.
There are 3 constraints, so $A, B, C$ will have 3 rows.

As the example is written, there are:
- an output term for each constraint (here $v_1, v_2, out$)
- a left term (here $x, v_1, v_2$)
- a right term (here $y, z, u$)

Each term will be represented by the matrix $A$, $B$ or $C$.
The results are:
$$\vec{w} = [1, out, x, y, z, u, v_1, v_2]$$
$$A = \begin{bmatrix}0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 \end{bmatrix}$$
$$B = \begin{bmatrix}0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 \end{bmatrix}$$
$$C = \begin{bmatrix}0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 \\ 0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 \end{bmatrix}$$


The [r1cs-ex2.py Python script](./r1cs-ex2.py) is available for this example.


### Example 3: Handling addition with constants

"Addition is free" in ZK SNARKs. We don't have to create additional constraint for addition operation.

$$out = x * y + 2 \Leftrightarrow out - 2 = x * y$$
$$\vec{w} = [1, out, x, y]$$
$$A = \begin{bmatrix}0 & 0 & 1 & 0 \end{bmatrix}$$
$$B = \begin{bmatrix}0 & 0 & 0 & 1 \end{bmatrix}$$
$$C = \begin{bmatrix}-2 & 1 & 0 & 0 \end{bmatrix}$$

The [r1cs-ex3.py Python script](./r1cs-ex3.py) is available for this example.

*Note: To multiply by a constant, the same can be done (if multiply by 2, then set 2 in the matrix value).*

### Example 4: Larger example

Let's use: $out = 3x^2y + 5xy -x - 2 y + 3$.

This expression will be divided into:
$$v_1 = 3x^2$$
$$v_2 = v_1 y$$
$$-v_2 + x + 2y - 3 + out = 5xy$$

Our $C \vec{w} = A \vec{w} * B \vec{w}$ results are:

$$\vec{w} = [1, out, x, y, v_1, v_2]$$
$$A = \begin{bmatrix}0 & 0 & 3 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 1 & 0 \\ 0 & 0 & 5 & 0 & 0 & 0 \end{bmatrix}$$
$$B = \begin{bmatrix}0 & 0 & 1 & 0 & 0 & 0 \\ 0 & 0 & 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 & 0 & 0 \end{bmatrix}$$
$$C = \begin{bmatrix}0 & 0 & 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 0 & 0 & 1 \\ -3 & 1 & 1 & 2 & 0 & -1 \end{bmatrix}$$


The [r1cs-ex4.py Python script](./r1cs-ex4.py) is available for this example.

## R1CS implementations
Real-world implementations use modular arithmetic instead of traditional arithmetic.

So, encoding for example $2/3$ is straightforward. It is $2 * 3^{-1}$. Those are easily done in modular arithmetic.

See the [r1cs-modular.py Python script](./r1cs-modular.py) for further testing.


## Circom Examples

### Circom implementation

In the circom language, math is done modulo $p = 21888242871839275222246405745257275088548364400416034343698204186575808495617$.

So, as the [r1cs-negativeCircom.py script]() shows, $-1 = p - 1$.


### Circom Example 1: Transforming out = x * y
Let's retake [Example 1](#example-1-transforming-out--x--y) with circom.

The file [circom-ex1.circom] can be compiled using `circom circom-ex1.circom --r1cs --sym`.

Then, details of the R1CS circuit can be seen with `snarkjs r1cs print circom-ex1.r1cs`.

The results will look different that our previous result. Circom solution is:
$$A = [0, 0, -1, 0]$$
$$B = [0, 0, 0, 1]$$
$$C = [0, -1, 0, 0]$$

The form is a little bit different. It is now $0 = A \vec{w} * B \vec{w} - C \vec{w}$.


To test the example, we will recompile it with `--wasm`. Then, we create the solution we want to test. We will test $x=41$ and $y=103$ as we did previously. . Finally, we can compute the witness.

```bash
# compile and create directory
circom circom-ex1.circom --r1cs --sym --wasm
# enter dir
pushd circom-ex1_js
# Write our x and y inputs
echo '{"x": "41", "y": "103"}' > input.json
# Generate the witness
node generate_witness.js circom-ex1.wasm input.json witness.wtns
# Export the witness as JSON
snarkjs wtns export json witness.wtns witness.json
# Check the witness against the R1CS circuit
snarkjs wtns check ../circom-ex1.r1cs witness.wtns
# print the witness
cat witness.json
# quit dir
popd
```
### Circom Example 2: Transforming out = x * y * z * u


The [circom-ex2.circom file](./circom-ex2.circom) translates this example in Circom language.


### Circom Example 4: Larger example
Let's use: $out = 3x^2y + 5xy -x - 2 y + 3$.

This expression will be divided into:
$$v_1 = 3x^2$$
$$v_2 = v_1 y$$
$$-v_2 + x + 2y - 3 + out = 5xy$$

The [circom-ex4.circom file](./circom-ex4.circom) translates those constraints in Circom language.

```bash
# compile and create directory
circom circom-ex4.circom --r1cs --sym --wasm
# enter dir
pushd circom-ex4_js
# Write our x and y inputs
echo '{"x": "1", "y": "2"}' > input.json
# Generate the witness
node generate_witness.js circom-ex4.wasm input.json witness.wtns
# Export the witness as JSON
snarkjs wtns export json witness.wtns witness.json
# Check the witness against the R1CS circuit
snarkjs wtns check ../circom-ex4.r1cs witness.wtns
# print the witness
cat witness.json
# quit dir
popd
```
