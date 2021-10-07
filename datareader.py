# Imports
import numpy as np
import statistics as s
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt

# Macros for code modularity
temp = 270
filelocation = './test0-270k/'
timestep = 1242.770 #timesteps/s for test0, slurm 1

#creating file locations
file1 = filelocation + 'slurm1'
file2 = filelocation + 'slurm2'
file3 = filelocation + 'slurm3'
file4 = filelocation + 'slurm4'
file5 = filelocation + 'slurm5'

# load the data file
slurm1_d = np.genfromtxt(file1, dtype=float, delimiter=(8, 13, 13, 13, 13, 13, 13, 13, 13, 15), skip_header = 60, skip_footer = 30, usecols = (-1), autostrip=True)
slurm2_d = np.genfromtxt(file2, dtype=float, delimiter=(8, 13, 13, 13, 13, 13, 13, 13, 13, 15), skip_header = 60, skip_footer = 30, usecols = (-1), autostrip=True)
slurm3_d = np.genfromtxt(file3, dtype=float, delimiter=(8, 13, 13, 13, 13, 13, 13, 13, 13, 15), skip_header = 60, skip_footer = 30, usecols = (-1), autostrip=True)
slurm4_d = np.genfromtxt(file4, dtype=float, delimiter=(8, 13, 13, 13, 13, 13, 13, 13, 13, 15), skip_header = 60, skip_footer = 30, usecols = (-1), autostrip=True)
slurm5_d = np.genfromtxt(file5, dtype=float, delimiter=(8, 13, 13, 13, 13, 13, 13, 13, 13, 15), skip_header = 60, skip_footer = 30, usecols = (-1), autostrip=True)

#array to number tests:
testNo = np.genfromtxt(file1, dtype=float, delimiter=(8, 13, 13, 13, 13, 13, 13, 13, 13, 15), skip_header = 60, skip_footer = 30, usecols = (0), autostrip=True)
time = testNo/timestep

#Calculating average density across the different runs:
length = len(testNo)
average_across = [0]*length
for i in range(length):
    average_across[i] = s.mean([slurm1_d[i], slurm2_d[i], slurm3_d[i], slurm4_d[i], slurm5_d[i]])

#Average density value from simulation
density = s.mean(average_across)
print("Density for " + str(temp) + ": " + str(density) + "\n") 

# Pruning of data - remove the first 100 entries (100 000 iterations)
#def delete_x_first_elements(arr, x):
    #copy = arr
    #for i in range(x):
     #   np.delete(copy, 0)
    #return copy

#s1f = delete_x_first_elements(slurm1_d, 100)
#print(s1f)
#print(len(s1f))

# plotting slurm1_d against t:
plt.plot(time, slurm1_d)
plt.savefig("t1_d270.png")

#Std Deviations:
print(s.stdev(average_across))
