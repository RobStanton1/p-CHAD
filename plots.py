import numpy as np
import matplotlib.pyplot as plt
from itertools import islice
import sys

def readData_1(datafile, nodeIndex, DERIndex, energyIndex):
    # this function prepares arrays for plotting
    # DER vs nodes, energy vs nodes

    with open(datafile) as d:
        
        nodes = []
        DER = []
        energy = []

        for line in islice(d, 1, None):
            splitLine = line.split()
            nodes.append(float(splitLine[nodeIndex]))
            DER.append(float(splitLine[DERIndex]))
            energy.append(float(splitLine[energyIndex])/1000.0) # Kilojoules
    
    return nodes, DER, energy
        
chdNodes, chdDER, chdEnergy = readData_1('chad.dat', 2, 13, 15)
lorNodes, lorDER, lorEnergy = readData_1('lorawan.dat', 2, 12, 14)

fig, ax = plt.subplots(figsize=(8, 5))

if int(sys.argv[1]) == 0:
    ax.plot(chdNodes, chdDER, label='CHAD DER')
    ax.plot(lorNodes, lorDER, label='LoRaWAN DER')
else:
    ax.plot(chdNodes, chdEnergy, label='CHAD Energy (KJ)')
    ax.plot(lorNodes, lorEnergy, label='LoRaWAN Energy (KJ)')

ax.legend(loc='best')
plt.show()