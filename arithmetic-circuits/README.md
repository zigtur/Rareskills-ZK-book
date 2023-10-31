# Arithmetic circuits

Zk circuits form a set of constraints that if satisfied, prove a computation was carried out correctly. Zk circuits are sometimes called arithmetic circuits because the “gates” in the circuit are addition and multiplication over a finite field.

Only addition and multiplication can be used as a **finite field** only has those 2 operations. Turning circuits to polynomial and EC points can then be easily done.

ZK circuits are used for validating a computation. As such, writing a ZK circuit is more like writing unit tests.

All maths done are over a finite field, (mod p) will most likely be omitted in the next sections.

## Example: Sudoku

A ZK circuit which verifies that a Sudoku is valid is developed as the following:
- each **column** contains every digit from 1 to 9 exactly once.
- each **row** contains every digit from 1 to 9exactly once.

Verifying the sudoku solution consists in checking that the proposed solution follows the rules.
In the case of the Sudoku, verifying that the solution is correct is a complete different algorithm than the solution algorithm.
Verification algorithm and solution algorithm are not always different, for example $5*7+3=38$ has the same algorithm for solution and verification.
Most of the time, the verification algorithm doesn't resemble the solving algorithm.


## Example: Proving b is the inverse of a
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

$a$ is a finite field element that falls in the range \[0;15\].

