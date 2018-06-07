


"""



"""


import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(5,3),columns=['col1','col2','col3'])
df.apply(np.mean,axis=1)
print (df.apply(np.mean))


"""

Its output is as follows −

     col1         col2         col3
	
0  0.543255    -1.613418    -0.500731   
           
1  0.976543    -1.135835    -0.719153   
                
2  0.184282    -0.721153    -2.876206    
              
3  0.447738     0.268062    -1.937888
                
4 -0.677673     0.177455     1.397360 


"""

