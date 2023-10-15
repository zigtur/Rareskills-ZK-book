# Set Theory

## Set - Definition

A set is a well-defined collection of objects.




## Cartesian product

### Exercise: BxA
- A = {1,2,3}
- B = {x, y, z}
- A × B = {(1, x), (1, y), (1, z), (2, x), …, (3, z)}
- B × A = {(x, 1), (x, 2), (x, 3), (y, 1), ..., (z, 3)}

### Exercise: Compute the cartesian product of {1,2,3,4} and {3,6,9,12} (in that order). If you were to pick 4 particular ordered pairs from this, what arithmetic computation would that encode?

- {(1, 3), (2, 6), (3, 9), (4, 12)}
- The arithmetic computation would be $(x * 3) = y$

## Subsets of the cartesian product form a function
In set-theoretic terms, a function is a subset of the cartesian product of the domain and codomain sets.


### Exercise: Define a mapping (function) from integers n ∈ 1,2,3,4,5,6 to the set {even, odd}.

## Injective, Surjective, and Bijective functions

- **Injective**: Elements in the codomain have at most one preimage. It can have zero or one preimage. We can also say that if an output element has a preimage, then it is unique.
- **Surjective**: Elements in the codomain has at least one preimage. If an element in the codomain does not have a preimage, the function is not surjective.
- **Bijective**: it is injective and surjective.

This is mainly based on how the domain and codomain is defined.



### Exercise: Let set A be {1,2,3} and set B be {x,y,z}. Define a function from A to B that is well-defined, but not surjective and not injective.
Solution: {(1,x) , (2,x) , (3, y)}



## A cartesian product of a set with itself


## Set relations
The phrase “taking a subset of the cartesian product” is so common that we have a word for it. It is a relation.

In the y = x² example, 2 from X is related to 4 from Y, but 3 in X is not related to 6.

## A “binary operator” in set theoretic terms

### Exercise: Pick a subset of ordered pairs that defines a * b mod 3.
|    |     (0,0)|     (1,0)|     (2,0)|     (0,1)|     (1,1)|     (2,1)|     (0,2)|     (1,2)|     (2,2)|
|----|----------|----------|----------|----------|----------|----------|----------|----------|----------|
| 0  |((0,0), 0)|((1,0), 0)|((2,0), 0)|((0,1), 0)|          |          |((0,2), 0)|          |          |
| 1  |          |          |          |          |((1,1), 1)|          |          |          |((2,2), 1)|
| 2  |          |          |          |          |          |((2,1), 2)|          |((1,2), 2)|          |



## Properties of binary operators over sets: Magma, Semigroups, and Monoids, and Groups

- A magma is a set with a closed binary operator. That’s it.
- A semigroup is a magma where the binary operator must be associative.
- A monoid is a semigroup with an identity element.


### Monoid

For example, addition over positive integers without zero is a semigroup, but if you include zero, it becomes a monoid.



### Exercise: Work out for yourself that concatenating “foo”, “bar”, “baz” in that order is associative. Remember, associative means (A op B) op C = A op (B op C).


### Exercise: Give an example of a magma and a semigroup. The magma must not be a semigroup. Don’t use the examples above.


## Unions and Intersection

If you take the union of two sets {1,2,3,4} and {3,4,5,6}, you get {1,2,3,4,5,6}. If you take the intersection of {1,2,3,4} and {3,4,5,6} you get {3, 4}.



## Group - The Star of the Show
A group is a monoid where each element has an inverse.

Or to be explicit, it is a set with three properties
- a closed and associative binary operator (a semigroup)
- an identity element (a monoid)
- every element has an inverse. That is, there exists an inverse element of the set such that the binary operator of an element and its inverse produces the identity element.


None of the algebraic data structures above are required to be commutative. If they are, we say they are abelian over their binary operator. So an abelian group means the binary operator is not sensitive to the order.


Abelian means the binary operator is commutative.

## Exercise: Why can’t strings under concatenation be a group?
Because there are no identity elements, so it can't be a monoid.

## Exercise: Polynomials under addition satisfy the property of a group. Demonstrate this is the case by showing it matches the three properties that define a group.


