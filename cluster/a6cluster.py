"""
Cluster class for k-Means clustering

This file contains the class cluster, which is the second part of the assignment.  With
this class done, the visualization can display the centroid of a single cluster.

YOUR NAME(S) AND NETID(S) HERE
DATE COMPLETED HERE
"""
import math
import random
import numpy


# For accessing the previous parts of the assignment
import a6checks
import a6dataset


class Cluster(object):
    """
    A class representing a cluster, a subset of the points in a dataset.

    A cluster is represented as a list of integers that give the indices in the dataset
    of the points contained in the cluster.  For instance, a cluster consisting of the
    points with indices 0, 4, and 5 in the dataset's data array would be represented by
    the index list [0,4,5].

    A cluster instance also contains a centroid that is used as part of the k-means
    algorithm.  This centroid is an n-D point (where n is the dimension of the dataset),
    represented as a list of n numbers, not as an index into the dataset. (This is because
    the centroid is generally not a point in the dataset, but rather is usually in between
    the data points.)

    INSTANCE ATTRIBUTES:
        _dataset [Dataset]: the dataset this cluster is a subset of
        _indices [list of int]: the indices of this cluster's points in the dataset
        _centroid [list of numbers]: the centroid of this cluster
    EXTRA INVARIANTS:
        len(_centroid) == _dataset.getDimension()
        0 <= _indices[i] < _dataset.getSize(), for all 0 <= i < len(_indices)
    """

    # Part A
    def __init__(self, dset, centroid):
        """
        Initializes a new empty cluster whose centroid is a copy of <centroid>

        Parameter dset: the dataset
        Precondition: dset is an instance of Dataset

        Parameter centroid: the cluster centroid
        Precondition: centroid is a list of ds.getDimension() numbers
        """
        self._dataset = dset
        self._indices = []
        result = []
        for x in centroid:
            result.append(x)
        self._centroid = result
        pass

    def getCentroid(self):
        """
        Returns the centroid of this cluster.

        This getter method is to protect access to the centroid.
        """
        return self._centroid

    def getIndices(self):
        """
        Returns the indices of points in this cluster

        This method returns the attribute _indices directly.  Any changes made to this
        list will modify the cluster.
        """
        return self._indices
        pass

    def addIndex(self, index):
        """
        Adds the given dataset index to this cluster.

        If the index is already in this cluster, this method leaves the
        cluster unchanged.

        Precondition: index is a valid index into this cluster's dataset.
        That is, index is an int in the range 0.._dataset.getSize()-1.
        """
        if index in self._indices:
            pass
        else:
            self._indices.append(index)
        pass

    def clear(self):
        """
        Removes all points from this cluster, but leave the centroid unchanged.
        """

        self._indices = []

        pass

    def getContents(self):
        """
        Returns a new list containing copies of the points in this cluster.

        The result is a list of list of numbers.  It has to be computed from the indices.
        """

        result = []
        for x in self._indices:
            #direct access?
            #list = self._dataset.getContents()
            #number = list[x]
            number = self._dataset.getPoint(x)
            result.append(number)
        return result
        #pass

    # Part B
    def distance(self, point):
        """
        Returns the euclidean distance from point to this cluster's centroid.

        Parameter point: The point to be measured
        Precondition: point is a list of numbers (int or float), with the same dimension
        as the centroid.
        """
        length = len(point)
        cats = []
        for x in range(length):
            value = (point[x] - self._centroid[x])**2
            cats.append(value)
        result = 0
        for y in cats:
            result = result + y
        return math.sqrt(result)

        pass

    def getRadius(self):
        """
        Returns the maximum distance from any point in this cluster, to the centroid.

        This method loops over the contents to find the maximum distance from
        the centroid.  If there are no points in this cluster, it returns 0.
        """
        if len(self._indices)==0:
            return 0

        list=[]

        contents=Cluster.getContents(self)

        for x in contents:
            value=Cluster.distance(self,x)
            list.append(value)

        result=0

        for y in list:
            if y>result:
                result=y

        return result

        pass

    def update(self):
        """
        Returns True if the centroid remains the same after recomputation; False otherwise.

        This method recomputes the _centroid attribute of this cluster. The new _centroid
        attribute is the average of the points of _contents (To average a point, average
        each coordinate separately).

        Whether the centroid "remained the same" after recomputation is determined by
        numpy.allclose.  The return value should be interpreted as an indication of whether
        the starting centroid was a "stable" position or not.

        If there are no points in the cluster, the centroid. does not change.
        """

        # IMPLEMENT ME
        #CHECK
        contents=self.getContents()

        what = self._centroid

        length=len(contents)
        dim=len(contents[0])



        #print("point is " + str(contents[0])

        coordsadded = []

        for x in range(dim):
            value=0
            for y in range(length):
                value=value+contents[y][x]
            coordsadded.append(value)

        print(coordsadded)

        self._centroid=[]
        for z in coordsadded:
                divide=z/length
                self._centroid.append(divide)

        #error here
        return numpy.allclose(self._centroid,what)





    # PROVIDED METHODS: Do not modify!
    def __str__(self):
        """
        Returns a String representation of the centroid of this cluster.
        """
        return str(self._centroid)

    def __repr__(self):
        """
        Returns an unambiguous representation of this cluster.
        """
        return str(self.__class__) + str(self)
