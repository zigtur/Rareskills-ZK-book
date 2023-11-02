from numpy import matmul

# Input to bit shift
a = [1,0,1,1]

# bit shift matrix
b = [[0,1,0,0],[0,0,1,0],[0,0,0,1],[0,0,0,0]]

# Result
c = [0,1,1,0]


print("1011 << 1 = 0110: ", matmul(b, a) == c)