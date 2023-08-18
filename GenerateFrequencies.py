import numpy as np
from Consts import hbar, Planck, c, muB, Sx4, Sy4, Sz4, SpinOp, SpinArray, S32, S12, S_12, S_32, SOT

class H0:
    def __init__(self, 
                 D = np.diag([0, 0, 2000])*(10**6),  
                 g = np.diag([2.00, 2.00, 2.25]), 
                 coil = np.array([0,0,320])*10**-3, 
                 MicrowaveField = np.array([1,1,0])):
        self.D = D
        print ("D = ", self.D)
        self.g = g
        print ("g = ", self.g)
        self.coil = coil
        print ("coil = ", self.coil)
        self.MicrowaveField = MicrowaveField
        print ("MicrowaveField = ", self.MicrowaveField)
        print ("Shape of SpinOp = ", SpinOp.shape)
        print ("Shape of SpinOp.T = ", SpinOp.T.shape)
        self.ZFS = np.einsum('i...,ij,j...', SOT, self.D, SpinOp)
        print ("ZFS = ", self.ZFS)
        self.Zeeman = muB * np.einsum('i...,ij,j...', SOT, g, self.coil)
        print ("Zeeman = ", self.Zeeman)
        self.Microwave = muB * np.einsum('i...,ij,j...', SOT, g, self.MicrowaveField)
        #https://encyclopedia.pub/entry/9965 Equation sources. 
        print ("Microwave = ", self.Microwave)
        self.H = self.ZFS + self.Zeeman + self.Microwave
        self.EigenValues, self.EigenVectors = np.linalg.eig(self.H)
        
a = H0()
print("Eignevalues are:",a.EigenValues)
print("Eigenvectors are:", round(3,a.EigenVectors))