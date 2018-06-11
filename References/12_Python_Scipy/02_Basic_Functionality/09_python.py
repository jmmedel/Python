


"""


Transpose of Matrix
This feature returns the transpose of self. Let us consider the following example.


"""


import numpy as np
mat = np.matrix('1 2; 3 4')
mat.T


"""

The above program will generate the following output.

matrix([[1, 3],
        [2, 4]])

When we transpose a matrix, we make a new matrix whose rows are the columns of the original. A conjugate transposition, on the other hand, interchanges the row and the column index for each matrix element. The inverse of a matrix is a matrix that, if multiplied with the original matrix, results in an identity matrix.


"""