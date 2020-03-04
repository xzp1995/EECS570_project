#python3
import numpy as np

LOW = 100 #lower bound of entries
HIGH = 200 #upper bound of entries

W = 5 #width of matrix
H = 5 #height of matrix

N = 1 #number of matrix pairs


# matrix = np.zeros((2 * N,W,H)).astype(int)
solutions = np.zeros((N,W,H)).astype(int)
results = np.zeros((N,W,H)).astype(int)

#read results and solutions files
for i in range(0,N):
    solutions[i] = np.fromfile("s_{}.bin".format(i), dtype=np.int).reshape(W,H)
    results[i] = np.fromfile("r_{}.bin".format(i), dtype=np.int).reshape(W,H)

print(np.array_equal(results, solutions))
