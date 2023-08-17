import numpy as np
from StateDev import State, Sx4, Sy4, Sz4, S32, S12, S_12, S_32, Planck, c, hbar

class Hamiltonian:
       def __init__(self, D = np.diag([0,0,2000])*10**6, g = np.array([1.9,1.9,2.25]), magField = 320*10**6):
              self.D = D
              self.g = g
              self.magField = magField
              self.States = {"S32":State(SpinVec=S32, magField=self.magField, D=self.D, g=self.g),
                             "S12":State(SpinVec=S12, magField=self.magField, D=self.D, g=self.g),
                             "S_12":State(SpinVec=S_12, magField=self.magField, D=self.D, g=self.g),
                             "S_32":State(SpinVec=S_32, magField=self.magField, D=self.D, g=self.g)}
              def Wavelength(E1, E2):
                     return Planck*c/(E1 - E2)
              self.Wavelengths = {}              
              for x in self.States:
                     for y in self.States:
                            if x != y: 
                                   self.Wavelengths[str(x)+ '-' + str(y)] = Wavelength(self.States[x].EnergyLevel, self.States[y].EnergyLevel)
              def Frequency(E1, E2):
                     return (E1 - E2)/Planck
              self.Frequencies = {}
              for x in self.States:
                     for y in self.States:
                            if x != y:
                                   self.Frequencies[str(x)+ '-' + str(y)] = Frequency(self.States[x].EnergyLevel, self.States[y].EnergyLevel)

a = Hamiltonian(D = np.diag([0,0,2000.0]) *10**6, g = np.diag([1.9, 1.8, 2.25]), magField = np.diag([0, 0, 320*(10**-3)]) )

#print(a.States["S32"].EnergyLevel)

#print(a.Wavelengths["S32-S12"]*100, "cm")
#print(a.Frequencies["S32-S12"]/10**9, "GHz")
