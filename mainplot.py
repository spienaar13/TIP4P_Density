# Imports
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt

# TIP4P/2005 literary data                                                                                                                                                                                 
temps = [270, 300, 330, 360]
data = [1.0010, 0.9965, 0.9841, 0.9668]
calcs = [1.0018, 0.9970, 0.9844, 0.9650]

# plot:
fig, ax = plt.subplots()
ax.plot(temps, data, label="Abasal+Vega data")
ax.plot(temps, calcs, label="Simulation")
ax.set_xlabel('Temperature (K)')
ax.set_ylabel('Density (g/cm^3)')
ax.set_title('TIP4P comparison')
ax.legend()
fig.savefig('mainplot.png')
