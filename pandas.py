import pandas as pd
import matplotlib.pyplot as plt
data=[100,120,140,180,200,210,214]
s=pd.Series(data,index=range(len(data)))
s=s.plot()
plt.show()
