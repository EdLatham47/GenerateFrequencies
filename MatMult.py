import numpy as np
from State import State, Sx4, Sy4, Sz4, S32, S12, S_12, S_32, Planck, c, hbar
# a File that makes a Hamiltonian for a given D, g, and magField
# D is the zero field splitting
# g is the g-factor
# magField is the magnetic field in Tesla
# The Hamiltonian is a dictionary of States
# it then computes the wavelengths and frequencies of the transitions between the states
#It also transforms these frequencies into Rabi Frequencies

class Hamiltonian:
       def __init__(self, D = 2000*(10**6), g = 2.25, magField = 320*10**6):
              self.D = D
              self.g = g
              self.magField = magField
              self.States = {"S32":State(SpinVec=S32, magField=self.magField, D=self.D, g=self.g),
                             "S12":State(SpinVec=S12, magField=self.magField, D=self.D, g=self.g),
                             "S-12":State(SpinVec=S_12, magField=self.magField, D=self.D, g=self.g),
                             "S-32":State(SpinVec=S_32, magField=self.magField, D=self.D, g=self.g)}
              
              Lowest = min([self.States["S32"].EnergyLevel, self.States["S12"].EnergyLevel, self.States["S-12"].EnergyLevel, self.States["S-32"].EnergyLevel])
              #print("Lowest Energy:", Lowest)
              for x in self.States:
                     self.States[x].EnergyLevel += -Lowest
              #print(self.States["S32"].EnergyLevel, self.States["S12"].EnergyLevel, self.States["S_12"].EnergyLevel, self.States["S_32"].EnergyLevel)
              
              def Wavelength(E1, E2):
                     return Planck*c/(E1 - E2)
              self.Wavelengths = {}              
              for x in self.States:
                     for y in self.States:
                            if int(x[1:]) > int(y[1:]):
                                   self.Wavelengths[str(x)+ '_' + str(y)] = Wavelength(self.States[x].EnergyLevel, self.States[y].EnergyLevel)
                                   
              def Frequency(E1, E2):
                     return (E1 - E2)/Planck
              self.Frequencies = {}
              self.TwoPiPulses = {}
              for x in self.States:
                     for y in self.States:
                            if int(x[1:]) > int(y[1:]):
                                   self.Frequencies[str(x)+ '_' + str(y)] = Frequency(self.States[x].EnergyLevel, self.States[y].EnergyLevel)
                                   self.TwoPiPulses[str(x)+ '_' + str(y)] = 1/(self.Frequencies[str(x)+ '_' + str(y)])

              def RabiFrequency(E1, E2):
                     return np.sqrt(2*np.pi*E1*E2/(hbar*Planck))
              self.RabiFrequencies = {}
              for x in self.States:
                     for y in self.States:
                            if int(x[1:]) > int(y[1:]):
                                   self.RabiFrequencies[str(x)+ '_' + str(y)] = RabiFrequency(self.States[x].EnergyLevel, self.States[y].EnergyLevel)

a = Hamiltonian(D = 600.0 * (10**6), g = 2.25, magField = 300 * (10**-3))

for x in a.States:
       print(x, a.States[x].EnergyLevel, "J")       
for x in a.Wavelengths:
       print(x, "    ", a.Wavelengths[x]/10**-9, "nm     ", a.Frequencies[x]/10**9, "GHz   ", a.TwoPiPulses[x], "s")
for x in a.RabiFrequencies:
       print(x, "    ", a.RabiFrequencies[x]/10**6, "MHz compared to", a.Frequencies[x]/10**6, "MHz")