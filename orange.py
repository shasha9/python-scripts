import pandas as pd
import matplotlib.pyplot as plt
fruits=['apple','mango','banana','cherries']
quantities=[20,30,52,10]
s=pd.Series(quantities,index=fruits)
s=s.plot()
plt.title("fruit chart")
plt.show()
