# Arithmetic circuits

Zk circuits form a set of constraints that if satisfied, prove a computation was carried out correctly. Zk circuits are sometimes called arithmetic circuits because the “gates” in the circuit are addition and multiplication over a finite field.

Only addition and multiplication can be used as a **finite field** only has those 2 operations. Turning circuits to polynomial and EC points can then be easily done.

ZK circuits are used for validating a computation. As such, writing a ZK circuit is more like writing unit tests.

All maths done are over a finite field, (mod p) will most likely be omitted in the next sections.

## Example: Sudoku

A ZK circuit which verifies that a Sudoku is valid is developed as the following:
- each **column** contains every digit from 1 to 9 exactly once.
- each **row** contains every digit from 1 to 9exactly once.

Verifying the sudoku solution consists in checking that the proposed solution follows the rules.
In the case of the Sudoku, verifying that the solution is correct is a complete different algorithm than the solution algorithm.
Verification algorithm and solution algorithm are not always different, for example $5*7+3=38$ has the same algorithm for solution and verification.
Most of the time, the verification algorithm doesn't resemble the solving algorithm.


## Example: Proving b is the inverse of a
The solving algorithm of this statement is $b=pow(a, -1, n)$, with $n$ being the size of the field.
When verifying, we do not do the computation and compare the result.
If $b$ is the inverse of $a$, then $a * b == 1$ and this is the verification algorithm.


A [Python implementation](./inverse.py) can be found.


## Example: Proving x is the root of a polynomial

*Note: Recall that most circuits do not have the same verifying and solving algorithms.
In this example, the algorithm is the same for booth solving and verifying.*

ZK circuits could have been called *systems of non-linear constraints* beause it's what they are. 

In our example, proving that $x=15$ is a root of $2x^2 - 35x + 75$ would be done through a circuit that looks like the computation:
`assert 0 == 2 (15)² - 35(15) + 75`.

ZK-circuits are non-linear. Modeling an arbitrary computation as a **linear** system of constraints would be a straightforward proof that $P=NP$ since linear systems of equations are easy to solve. If $P=NP$, there isn’t any significant compute cost difference in proving the equation rather than solving it.

## Example: Proving a binary transformation was valid

$a$ is a finite field element that falls in the range \[0;15\]. Claim is $b1, b2, b3, b4$ is the binary representation of $a$. For example, $a=11$ then $(b1, b2, b3, b4) = (1,0,1,1)$.

In an arithmetic circuit, everything is a field element. So, we need to be sure that all $b1, b2, b3, b4$ have value $0$ or $1$. To constrain this, the following code can be used:
```
b1 * (1 - b1) == 0
b2 * (1 - b2) == 0
b3 * (1 - b3) == 0
b4 * (1 - b4) == 0
```
*Note: If any of the $b*$ value is different than 1 or 0, then one of the check will fail.*

The next step is to prove that the combination of all $b*$ is equal to $a$.
```
(8 * b1) + (4 * b2) + (2 * b3) + (1 * b4) == 11
```

Here we didn't recompute the binary transformation (solving algorithm) but we verified it is true (verifying algorithm).

## Example: Proving a number falls into a certain range
Using the binary transformation used before, we can prove that a number falls into the interval $[0, 2^n-1]$ where $n$ is the number of bits. If the sum of all bits isn't equal to the number, then the number must be outside the range.

```
Claim: a is in the range [0, 255]

Proof: bi * (1 - bi) == 0 for i in [1…8] and (128 * b1) + (64 * b2) + … + (1 * b8) == a
```


## Example: Proving a > b
This comparison can't be done easily with only addition and multiplication.
Comparison operators traditionally used are not consistent over finite fields, when overflow and underflow are common.
For example, $1 < (1-2)$ will lead to inconsistencies.

This will be explained in a future part of ZK book.

## Example: Proving x is the maximum element in a list of elements
This requires the previous example about comparison.

## Example: Proving integer division was done properly
For finite field division, it can be done the same way as [the first example explained](#example-proving-b-is-the-inverse-of-a).

If we want to prove integer division, this part can become tricky. $7/2 = 3$, but $2*3 \neq 7$. So, we need to verify two claims:
- $3$ is the quotient of $7/2$
- $1$ is the remainder of $7/2$

In this case, the first constraint would be $quotient * divisor + remainder == numerator$. But it's not sufficient, a malicious prover could use $2*2 + 3 == 7$.

The second constraint to implement is that $remainder < divisor$. This require the [comparison circuit](#example-proving-a--b).


## Example: Proving a list was sorted

If a prover claims that the list B is the list A that has been sorted, then:
- A and B have the same length
- B is itself sorted
- A and B have the same elements

The first two checks can be done using the previous examples.
To avoid computing the mapping ourselves, we ask the prover to give us the mapping from unsorted list to sorther list.
Then, we just verify the mapping is valid. It can be done with matrix multiplication for example.
$$\begin{bmatrix} 0 & 1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} 5 \\ 4 \\ 6 \end{bmatrix} = \begin{bmatrix} 4 \\ 5 \\ 6 \end{bmatrix}$$

To verify the “transformation matrix” is valid, we need to ensure each element is zero or one, and each row and column contains exactly one “1” with the rest being zeros.


## Example: proving a bit shift

To prove a bitshift, a matrix multiplication can be used like it has been done to prove a list was sorted.
This time, the matrix will have all the "1" elements sit on a diagonal.
This will prove the permutation is a bit shift.
The bit shift matrix for 4 bit is $\begin{bmatrix} 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 0 & 0 \end{bmatrix}$.

A [Python script](./bitshift.py) shows a 4-bit example.


## Example: List contains no duplicates
To check that a list contains no duplicates, the list is turned into a set and the size of the set is checked to see if equal to the size of the list.

Otherwise, we ask the prover to sort the list, verify it is sorted and then check each element to see if previous element is equal.

## Hash functions

Cryptographic hash functions are largely a combination of bitshifts and bit-wise XOR operations.

If each step of the hash function can be proven to have been executed correctly, then the entire hash function can be proven as executed correctly.
And this, without executing the hash function.


## Conclusion

Principle: “if a claimed output of a computation is true, then the output must have requirements that are satisfied.
If the requirements are hard to model with only addition or multiplication, we ask the prover to
auxiliary work so we can model the requirements more easily.”

