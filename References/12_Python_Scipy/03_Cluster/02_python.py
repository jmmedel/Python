


"""

Compute K-Means with Three Clusters
Let us now compute K-Means with three clusters using the following code.

# computing K-Means with K = 3 (2 clusters)
centroids,_ = kmeans(data,3)
The above code performs K-Means on a set of observation vectors forming K clusters. The K-Means algorithm adjusts the centroids until sufficient progress cannot be made, i.e. the change in distortion, since the last iteration is less than some threshold. Here, we can observe the centroid of the cluster by printing the centroids variable using the code given below.

print(centroids)
The above code will generate the following output.

print(centroids)[ [ 2.26034702  1.43924335  1.3697022 ]
                  [ 2.63788572  2.81446462  2.85163854]
                  [ 0.73507256  1.30801855  1.44477558] ]
Assign each value to a cluster by using the code given below.

# assign each sample to a cluster
clx,_ = vq(data,centroids)
The vq function compares each observation vector in the ‘M’ by ‘N’ obs array with the centroids and assigns the observation to the closest cluster. It returns the cluster of each observation and the distortion. We can check the distortion as well. Let us check the cluster of each observation using the following code.


"""


# check clusters of observation
print (clx)
