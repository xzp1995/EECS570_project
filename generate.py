#python3
import numpy as np

LOW = 100 #lower bound of entries
HIGH = 200 #upper bound of entries

W = 5 #width of matrix
H = 5 #height of matrix

N = 3 #number of matrix pairs


matrix = np.zeros((2 * N,W,H)).astype(int)
solutions = np.zeros((N,W,H)).astype(int)
# results = np.zeros((N,W,H)).astype(int)

#generate matrix and solutions
for i in range(0,N):
    matrix[2 * i] = np.random.randint(HIGH, size = (W,H), dtype=int)
    matrix[2 * i].tofile("m_{}.bin".format(2 * i))
    matrix[2 * i + 1] = np.random.randint(HIGH, size = (W,H), dtype=int)
    matrix[2 * i + 1].tofile("m_{}.bin".format(2 * i + 1))
    solutions[i] = matrix[2 * i].dot(matrix[2 * i + 1])
    solutions[i].tofile("s_{}.bin".format(i))
    solutions[i].tofile("r_{}.bin".format(i)) #r_{} should be generated in verilog

print(np.fromfile("m_0.bin",  dtype=np.int).reshape(W,H))
print(np.fromfile("m_1.bin",  dtype=np.int).reshape(W,H))
print(np.fromfile("s_0.bin",  dtype=np.int).reshape(W,H))
print(np.fromfile("r_0.bin",  dtype=np.int).reshape(W,H))
