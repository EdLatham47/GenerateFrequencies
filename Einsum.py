import numpy as np

A = np.array([[[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]],
              [[2,2,2,2],[2,2,2,2],[2,2,2,2],[2,2,2,2]],
             [[3,3,3,3,],[3,3,3,3],[3,3,3,3],[3,3,3,3]]])


B = np.array([[1,2,3],[4,5,6],[7,8,9]])

#C = np.einsum('ii,ikl', B, A)
C = np.einsum(B, [0,1], A, [1,2,3])
print(C)
print(C.shape)
print(A.T.shape)


D = A @ C
print(D.shape)
print(D)


#D = np.einsum('...i,i...',A.T, C)
