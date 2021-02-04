from dwave_qbsolv import QBSolv
import numpy as np
import pickle
import math

#number of variables
n = 12
file = open("rou12.QUBO", "rb")
QUBO = pickle.load(file)
file.close()
file = open("rou12.flow", "rb")
flows = pickle.load(file)
file.close()
file = open("rou12.dist", "rb")
distances = pickle.load(file)
file.close()

result = QBSolv().sample_qubo(QUBO, num_repeats=50, verbosity=0,  solver='tabu')
samples = list(result.samples())
perm = np.zeros((n,), dtype=int)
solution = ""
cost = 0
for i in range(n):
    for j in range(n):
        if samples[0][(i*n)+j] == 1:
            solution = solution + " " + str(j+1)
            perm[i]=j+1

print("solution", ":", solution)
for i in range(n):
    for j in range(n):
        cost += distances[i,j]*flows[int(perm[i]-1),int(perm[j])-1]
print("cost:", cost)


