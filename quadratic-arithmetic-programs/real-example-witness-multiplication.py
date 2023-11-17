import numpy as np
Ua = np.array([[0, 0, 0.5, -1, 0, 2],
                [0, 0, -2.5, 4, 0, -6],
                [0, 0, 3, -3, 0, 4]])

witness = [1, 199, 3, 4, 9, 16]

print("Result: U =", np.matmul(Ua, witness))
# array([ 29.5, -87.5,  61. ])

Va = np.array([[0, 0, 1, -1, 0, 0],
                 [0, 0, -4, 4, 0, 0],
                 [0, 0, 4, -3, 0, 0]])
                 
print("Result: V =", np.matmul(Va, witness))
# array([-1,  4,  0])

Wa = np.array([[1, 0.5, 0, 0, 0, -1],
                 [-3, -1.5, 0, 0, -1, 4],
                 [2, 1, 0, 0, 2, -3]])
                 
print("Result: W =", np.matmul(Wa, witness))
# array([  84.5, -246.5,  171. ])