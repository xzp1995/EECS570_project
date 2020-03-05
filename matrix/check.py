#python3
import filecmp

N = 1 #number of matrix pairs

#read results and solutions files
for i in range(0,N):
    if not filecmp.cmp("s_{}.txt".format(i), "r_{}.txt".format(i)):
        print("#{} pair is not correct".format(i))
        assert(0)
        
print("all results are correct")
