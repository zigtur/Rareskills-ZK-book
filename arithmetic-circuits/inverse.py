field_size = 29 # some prime number

## Prover
def compute_inverse(a):
    return pow(a, -1, field_size)

a = 22
b = compute_inverse(a)
print("In field", str(field_size), "the inverse of a (value: 22) is:", str(b))

## Verifier
assert (a * b) % field_size == 1
print("a * b == 1:", (a * b) % field_size == 1)

