import numpy as np
from scipy.constants import hbar, Planck, c
muB = 9.274009994*10**-24

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
S32 = np.array([1, 0,0,0])
S12 = np.array([0, 1,0,0])
S_12 = np.array([0, 0,1,0])
S_32 = np.array([0, 0,0,1])

class State():
    def __init__(self, SpinVec, EnergyLevel = 0.0, magField = 0.0**10**-3, D = 2000*(10**6), g = 2.25, name = "State" ):
        self.SpinVec = SpinVec
        self.D = D
        self.g = g
        self.name = name
        self.magField = magField
        self.EnergyLevel = hbar *  self.D * self.SpinVec.T @ (Sz4 @ Sz4) @ self.SpinVec + muB * self.g * self.magField * self.SpinVec.T @ Sz4 @ self.SpinVec
    
    
    def __repr__(self):
        return "StateVec: {}, EnergyLevel: {}, Spin: {}, magField: {}, D: {}, gz: {}".format(self.SpinVec, self.EnergyLevel, self.magField, self.D, self.gz)
    