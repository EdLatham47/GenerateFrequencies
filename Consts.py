from scipy.constants import hbar, Planck, c
import numpy as np
muB = 9.274009994*10**-24
print("hbar: ", hbar)
print("Planck: ", Planck)
print("c: ", c)
print("muB: ", muB)
#Sz Basis
S32 = np.array([1, 0,0,0])
S12 = np.array([0, 1,0,0])
S_12 = np.array([0, 0,1,0])
S_32 = np.array([0, 0,0,1])
SpinArray = np.array([S32, S12, S_12, S_32])

Sx4 = 1/2*np.array([[0, np.sqrt(3), 0, 0],
        [np.sqrt(3), 0, 2, 0],
        [0, 2, 0, np.sqrt(3)],
        [0, 0, np.sqrt(3), 0]])
Sy4 = 1/2*np.array([[0, -np.sqrt(3)*1j, 0, 0],
       [np.sqrt(3)*1j, 0, -2j, 0],
       [0, 2j, 0, -np.sqrt(3)*1j],
       [0,0,np.sqrt(3)*1j, 0]])
Sz4 = 1/2*np.array([[3,0,0,0],
       [0,1,0,0],
       [0,0,-1,0],
       [0,0,0,-3]])
SpinOp = np.array([Sx4, Sy4, Sz4])
SOT = SpinOp.transpose(0,2,1)
