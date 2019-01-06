"""
Primary algorithm for k-Means clustering

This file contains the Algorithm class for performing k-means clustering.  While it is
the last part of the assignment, it is the heart of the clustering algorithm.  You
need this class to view the complete visualizer.

YOUR NAME(S) AND NETID(S) HERE
DATE COMPLETED HERE
"""
import math
import random
import numpy


# For accessing the previous parts of the assignment
import a6checks
import a6dataset
import a6cluster


class Algorithm(object):
    """
    A class to manage and run the k-means algorithm.

    INSTANCE ATTRIBUTES:
        _dataset [Dataset]: the dataset which this is a clustering of
        _clusters [list of Cluster]: the clusters in this clustering (not empty)
    """

    # Part A
    def __init__(self, dset, k, seeds=None):
        """
        Initializes the algorithm for the dataset ds, using k clusters.

        If the optional argument seeds is supplied, it will be a list of indices into the
        dataset that specifies which points should be the initial cluster centroids.
        Otherwise, the clusters are initialized by randomly selecting k different points
        from the database to be the cluster centroids.

        Parameter dset: the dataset
        Precondition: dset is an instance of Dataset

        Parameter k: the number of clusters
        Precondition: k is an int, 0 < k <= dset.getSize()

        Paramter seeds: the initial cluster indices (OPTIONAL)
        Precondition seeds is None, or a list of k valid indices into dset.
        """

        self._dataset = dset
        dataset1 = a6dataset.Dataset.getContents(self._dataset)


        if not seeds is None:
            clusters = []
            for x in seeds:
                fuck = a6cluster.Cluster(self._dataset, dataset1[x])
                clusters.append(fuck)

        else:
            centroid = random.sample(list(dataset1), k)
            clusters = []
            for x in centroid:
                cats = a6cluster.Cluster(self._dataset, x)
                clusters.append(cats)
        self._clusters = clusters



    def getClusters(self):
        """
        Returns the list of clusters in this object.

        This method returns the attribute _clusters directly.  Any changes made to this
        list will modify the set of clusters.
        """
        return self._clusters
        pass

    # Part B
    def _nearest(self, point):
        """
        Returns the cluster nearest to point

        This method uses the distance method of each Cluster to compute the distance
        between point and the cluster centroid. It returns the Cluster that is closest.

        Ties are broken in favor of clusters occurring earlier self._clusters.

        Parameter point: The point to compare.
        Precondition: point is a list of numbers (int or float), with the same dimension
        as the dataset.
        """
        result = self._clusters[0]
        dist1 = self._clusters[0].distance(point)
        for x in self._clusters:
            dist = x.distance(point)
            if dist < dist1:
                dist1 = dist
                result = x
        return result


    def _partition(self):
        """
        Repartitions the dataset so each point is in exactly one Cluster.
        """
        # First, clear each cluster of its points.  Then, for each point in the
        # dataset, find the nearest cluster and add the point to that cluster.

        for x in self._clusters:
            x.clear()
        dataset1 = a6dataset.Dataset.getContents(self._dataset)
        for y in dataset1:
            cats = self._nearest(y)
            index = dataset1.index(y)
            cats.addIndex(index)

    # Part C
    def _update(self):
        """
        Returns true if all centroids are unchanged after an update; False otherwise.

        This method first updates the centroids of all clusters'.  When it is done, it
        checks whether any of them have changed. It then returns the appropriate value.
        """
        result = True

        for x in self._clusters:
            result = x.update()
            if result == False:
                result = False
        return result


    def step(self):
        """
        Returns True if the algorithm converges after one step; False otherwise.

        This method performs one cycle of the k-means algorithm. It then checks if
        the algorithm has converged and returns the appropriate value.
        """
        # In a cycle, we partition the points and then update the means.
        # IMPLEMENT ME
        self._partition()
        return self._update()

        pass

    # Part D
    def run(self, maxstep):
        """
        Continues clustering until either it converges or maxstep steps
        (which ever comes first).

        This method calls step() repeatedly, up to maxstep times, until the
        algorithm converges. It stops after maxstep iterations even if the
        algorithm has not converged.

        Parameter maxstep: the maximum number of steps to try
        Precondition: maxstep is an int >= 0
        """
        # You do not need a while loop for this.  Just write a for-loop, and exit
        # the for-loop (with a return) if you finish early.
        # IMPLEMENT ME
        for k in range(maxstep):
            if self.step() == True:
                return self.step()
        pass
