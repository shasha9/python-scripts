import numpy as np
x=np.array([[1,2,3],
            [4,5,6],
            [7,8,9]],np.int32)
np.savetxt("test.txt",x)
print("file saved success")
