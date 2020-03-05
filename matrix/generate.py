#python3
import numpy as np

LOW = 100 #lower bound of entries
HIGH = 200 #upper bound of entries

W = 3 #width of matrix
H = W #height of matrix

N = 1 #number of matrix pairs


matrix = np.zeros((2 * N,W,H)).astype(int)
solutions = np.zeros((N,W,H)).astype(int)
# results = np.zeros((N,W,H)).astype(int)

#generate matrix and solutions
for i in range(0,N):
    matrix[2 * i] = np.random.randint(LOW, HIGH, size = (W,H), dtype=int)
    a = np.zeros((W + H, H)).astype(int)
    for j in range(0,W):
        for k in range(0, H):
            a[j + k, j] = matrix[2 * i, j, k]
    np.savetxt("oa_{}.txt".format(i), matrix[2 * i].reshape(W * H, 1), fmt = '%d')
    np.savetxt("a_{}.txt".format(i), a.reshape((W + H) * H, 1), fmt = '%d')

    matrix[2 * i + 1] = np.random.randint(HIGH, size = (W,H), dtype=int)
    b = np.zeros((W + H, H)).astype(int)
    for j in range(0,W):
        for k in range(0, H):
            b[j + k, j] = matrix[2 * i + 1, k, j]
    np.savetxt("ob_{}.txt".format(i), matrix[2 * i].reshape(W * H, 1), fmt = '%d')
    np.savetxt("b_{}.txt".format(i), a.reshape((W + H) * H, 1), fmt = '%d')

    solutions[i] = matrix[2 * i].dot(matrix[2 * i + 1])
    np.savetxt("s_{}.txt".format(i), solutions[i].reshape(W * H, 1), fmt = '%d')
    np.savetxt("r_{}.txt".format(i), solutions[i].reshape(W * H, 1), fmt = '%d')

