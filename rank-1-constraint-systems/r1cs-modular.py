p = 23

# 2 * 3^-1 mod p
two_thirds = 2 * pow(3, -1, p)

assert (two_thirds * 3) % p == 2

# ⅓ = 3 * 1^-1
one_third = pow(3, -1, p)

# check that ⅓ + ⅔ == 1 mod p
assert (two_thirds + one_third) % p == 1