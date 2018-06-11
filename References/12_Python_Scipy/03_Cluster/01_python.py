


"""
SciPy - Cluster

K-means clustering is a method for finding clusters and cluster centers in a set of unlabelled data. Intuitively, we might think of a cluster as – comprising of a group of data points, whose inter-point distances are small compared with the distances to points outside of the cluster. Given an initial set of K centers, the K-means algorithm iterates the following two steps −

For each center, the subset of training points (its cluster) that is closer to it is identified than any other center.

The mean of each feature for the data points in each cluster are computed, and this mean vector becomes the new center for that cluster.

These two steps are iterated until the centers no longer move or the assignments no longer change. Then, a new point x can be assigned to the cluster of the closest prototype. The SciPy library provides a good implementation of the K-Means algorithm through the cluster package. Let us understand how to use it.

K-Means Implementation in SciPy
We will understand how to implement K-Means in SciPy.

Import K-Means
We will see the implementation and usage of each imported function.

from SciPy.cluster.vq import kmeans,vq,whiten
Data generation
We have to simulate some data to explore the clustering.



"""

from numpy import vstack,array
from numpy.random import rand

# data generation with three features
data = vstack((rand(100,3) + array([.5,.5,.5]),rand(100,3)))

"""

Now, we have to check for data. The above program will generate the following output.

array([[ 1.48598868e+00, 8.17445796e-01, 1.00834051e+00],
       [ 8.45299768e-01, 1.35450732e+00, 8.66323621e-01],
       [ 1.27725864e+00, 1.00622682e+00, 8.43735610e-01],
       …………….

Normalize a group of observations on a per feature basis. Before running K-Means, it is beneficial to rescale each feature dimension of the observation set with whitening. Each feature is divided by its standard deviation across all observations to give it unit variance.

Whiten the data
We have to use the following code to whiten the data.

# whitening of data
data = whiten(data)

"""




