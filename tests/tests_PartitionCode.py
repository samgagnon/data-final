import unittest
import nose.tools as nt
import numpy as np 
import PartitionCode as pc

class test_PartitionCode():

    def setUp(self):
        #A sample map array of length 8
        self.mapArray = [[1,1,1,1,1,1,1,1]]
        #Slices that should work and shouldn't
        self.badNumSlices = 3
        self.goodNumSlices = 4

        #Weight tests
        self.weightArray1 = np.asarray([[1]])

    def tearDown(self):
        pass


    
    def test_slicingError(self):
        '''
        Tests the slicing function to make sure it
        knows what a bad amount of slices are
        '''
        nt.assert_raises(TypeError, pc.sliceFixer,self.badNumSlices,self.mapArray)

    def test_slicingPartitions(self):
        '''
        Tests the slicing function to make sure it is 
        returning the right partition
        '''

        slicedMap = pc.sliceFixer(self.goodNumSlices, self.mapArray)
        nt.assert_equals([[[1, 1]], [[1, 1]], [[1, 1]], [[1, 1]]], slicedMap)

    def test_weightTestOne(self):
        '''
        Tests to make sure if the weight function only gets a single arguement, (map),
        it returns a weight of one
        '''
        weight = pc.slicedWeightGetter(self.weightArray1)[0]
        nt.assert_equals(1.0,weight)

