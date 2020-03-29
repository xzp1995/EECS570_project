#python3
import numpy as np
import time

LOW = 100 #lower bound of entries
HIGH = 200 #upper bound of entries

W = 1000 #width of matrix
H = W #height of matrix

N = 100 #number of matrix pairs

start = time.time()

for i in range(0,N):
    a = np.random.randint(LOW, HIGH, size = (W,H), dtype=int)
    b = np.random.randint(LOW, HIGH, size = (W,H), dtype=int)
    c = a.dot(b)

print("time: %s sec" % (time.time() - start))

