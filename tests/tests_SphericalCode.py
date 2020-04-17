#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import nose.tools as nt
import numpy as np 
import SphericalCode as sc

class test_SphericalCode():

    def setUp(self):
        #A sample map array of length 7
        self.mapArray = [[1,1,1,1,1,1,1]]
        self.expectedOutputSize = 1025

    def tearDown(self):
        pass
    
    def test_outputLength(self):
        # test full method to assert it returns a reasonable map size
        nt.assert_equal(sc.processMapSpherical, self.expectedOutputSize)

