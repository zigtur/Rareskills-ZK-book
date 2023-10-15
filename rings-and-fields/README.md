# Rings and Fields


## Ring
It is a set with two binary operators such that:
- under first binary operator, the set is an abelian group
- under second binary operator, the set is a monoid
    - Monoid: only the inverse property is missing to make it a group
    - if monoid is commutative, then it is an **abelian ring**
- second binary distributes over the first

The following must be true for the field:

```
(a □ b) ☆ c = (a ☆ c) □ (b ☆ c)
c ☆ (a □ b) = (c ☆ a) □ (c ☆ b)
```

But this is not necessarily true: `(a □ b) ☆ c = c ☆ (a □ b)`, because `☆` and is not always commutative unlike `□` (abelian group for first bin operator, not necessarily the second).


### Example rings
- Trivial ring with only {0} under addition and multiplication
- Set of all polynomials
    - First binary operator, addition:
        - If you add two polynomials together, you get another polynomial (closed and associative)
        - Inverse of an elements is the coeff multiplied by $-1$
        - Adding two polynomials with inverted coef, you get the additive identity $0$
    - Second, multiplication:
        - identity element is 1
        - inverses do not exist (not valid polynomials)
        - obviously closed and associative
- Square matrices of real numbers under addition and multiplication is a ring

## Field
It is a set with two bin operators such that:
- under the first, the set is an abelian group
- under the second (excluding the zero element), the set is an abelian group

### Example fields
- The set of all rational numbers is a field
    - Rational numbers are an abelian group under addition, this should be obvious.
    - They are also an abelian group under multiplication, if you remove zero. 
    - Without zero, every element has an inverse that produces the identity element 1.
- The set of all real numbers is a field
    - just like all retional numbers
    - In the previous examples: Real numbers are a field extension of rational numbers, and rational numbers are a subfield of real numbers.
- Integers modulo a prime number is a field under addition and multiplication


## Finite fields
Those are used a lot in cryptography.



