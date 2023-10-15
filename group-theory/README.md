# Group theory

Group is a set with:
* an associative and closed binary operator
* an identity element
* every element has an inverse

An Abelian group has the additional requirement:
* the binary operator is commutative



## Order of a group

The order of a group is just the number of elements in it.


## Cyclic groups

A cyclic group is a group that has an element that can generate all the others by applying binary operator repeatedly to that element or its inverse. It is generally called $g$ or $G$.

If a group is cyclic, then it is abelian:
- $R = P + Q$
- $R = (g+g+g+...+g) + (g+...+g)$, so we can invert $P$ and $Q$

The inverse statement isn't always true.


## Group Homomorphisms

Let A be a group with binary operator □ and B be a group with binary operator △.

Group A is homomorphic to group B if there exists a transformation φ where φ maps elements from A to B, and for all a, a’ in A, φ(a □ a’) = φ(a) △ φ(a’).


#### Example:
Sets:
- integers under addition
- powers of 2 under multiplication

Then, then transformation $\phi(x)$ is $2^i$. For all integers: $2^{a+b} = 2^a * 2^b$. This is also an *isomorphism*, because it works in both directions. For ZKP, we are interested in homomorphism.



If our transformation φ is cryptographically hard to invert, then we have homomorphic encryption. That is, we can apply binary operators to encrypted data and “do valid math” but not know what the original values were.



## Product of groups
It is possible to take the product of two groups (as they are special sets).

The product of two groups is a **group**.




