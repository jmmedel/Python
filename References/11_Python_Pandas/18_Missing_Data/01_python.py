


"""

Python Pandas - Missing Data

Missing data is always a problem in real life scenarios. Areas like machine learning and data mining face severe issues in the accuracy of their model predictions because of poor quality of data caused by missing values. In these areas, missing value treatment is a major point of focus to make their models more accurate and valid.

When and Why Is Data Missed?
Let us consider an online survey for a product. Many a times, people do not share all the information related to them. Few people share their experience, but not how long they are using the product; few people share how long they are using the product, their experience but not their contact information. Thus, in some or the other way a part of data is always missing, and this is very common in real time.

Let us now see how we can handle missing values (say NA or NaN) using Pandas.


"""

# import the pandas library
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(5, 3), index=['a', 'c', 'e', 'f',
'h'],columns=['one', 'two', 'three'])

df = df.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])

print (df)


"""

Its output is as follows −

         one        two      three
a   0.077988   0.476149   0.965836
b        NaN        NaN        NaN
c  -0.390208  -0.551605  -2.301950
d        NaN        NaN        NaN
e  -2.000303  -0.788201   1.510072
f  -0.930230  -0.670473   1.146615
g        NaN        NaN        NaN
h   0.085100   0.532791   0.887415
Using reindexing, we have created a DataFrame with missing values. In the output, NaN means Not a Number.

"""
