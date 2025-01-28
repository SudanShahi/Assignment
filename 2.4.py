import numpy as np

A=np.array([
    [1,2,3],
    [0,1,4],
    [5,6,0]
    ])

A_inv=np.linalg.inv(A)
identify_1 = np.dot(A_inv,A)
identify_2 = np.dot(identify_1,A)
print('Matrix A:\n',A)
print(A)
print('Matrix identify_1:\n',identify_1)
print(A_inv)
print("\nA_inv:\n",A_inv)
print(identify_2)
print("\nCheck if A *A^-1 is approximately identity matrix.")
print("Check if A *A^-1 is approximately identity matrix.")