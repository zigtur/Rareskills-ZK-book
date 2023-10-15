from libnum import has_sqrtmod_prime_power, sqrtmod_prime_power

# the functions take arguments# has_sqrtmod_prime_power(n, field_mod, k), where n**k,
# but we aren't interested in powers in modular fields, so we set k = 1
# check if sqrt(8) mod 11 exists
print(has_sqrtmod_prime_power(8, 11, 1))
# False

# check if sqrt(5) mod 11 exists
print(has_sqrtmod_prime_power(5, 11, 1))
# True

# compute sqrt(5) mod 11
print(list(sqrtmod_prime_power(5, 11, 1)))
# [4, 7]

assert (4 ** 2) % 11 == 5
assert (7 ** 2) % 11 == 5

# we expect 4 and 7 to be inverses of each other, because in "regular" math, the two solutions to a square root are sqrt and -sqrt
assert (4 + 7) % 11 == 0