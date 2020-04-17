#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 12:13:13 2020

@author: louiscroquette
"""

import matplotlib.pyplot as plt
import numpy as np
import healpy as hp


def wLCalc(cL, e):
    return (np.linalg.inv(cL)@e) / (e.T@np.linalg.inv(cL)@e)


# download raw data
planck30 = hp.read_map('../Desktop/LFI_SkyMap_030_1024_R2.01_full.fits')
planck44 = hp.read_map('../Desktop/LFI_SkyMap_044_1024_R2.01_full.fits')
planck70 = hp.read_map('../Desktop/LFI_SkyMap_070_1024_R2.01_full.fits')
planck100 = hp.read_map('../Desktop/HFI_SkyMap_100_2048_R2.02_full.fits')
planck143 = hp.read_map('../Desktop/HFI_SkyMap_143_2048_R2.02_full.fits')
planck217 = hp.read_map('../Desktop/HFI_SkyMap_217_2048_R2.02_full.fits')
planck353 = hp.read_map('../Desktop/HFI_SkyMap_353_2048_R2.02_full.fits')


# lower the resolution of the maps
planck30 = hp.ud_grade(planck30, 512)
planck44 = hp.ud_grade(planck44, 512)
planck70 = hp.ud_grade(planck70, 512)
planck100 = hp.ud_grade(planck100, 512)
planck143 = hp.ud_grade(planck143, 512)
planck217 = hp.ud_grade(planck217, 512)
planck353 = hp.ud_grade(planck353, 512)

map_array_old = np.array([planck30, planck44, planck70, planck100, planck143, planck217, planck353])
e = np.ones(len(map_array_old))

# example plot of raw data
hp.mollview(planck217, nest=False)


def processMapSpherical(map_array):
    sph_map_array = []
    for i in map_array: 
        sph_map_array.append(hp.sphtfunc.map2alm(i, lmax = 1024))
    
    cLArray = np.zeros((7,7,1025))
    countI = 0
    countJ = 0
    for i in map_array:
        countJ = 0
        for j in map_array:
            element = hp.sphtfunc.anafast(i, map2 = j, lmax = 1024)
            #print(element)
            cLArray[countI, countJ] = element
            countJ += 1
        countI += 1
        
    wLArray = np.zeros((7,1025))
    
    countI = 0
    while countI < 1025:
        wLArray[:,countI] = wLCalc(cLArray[:,:,countI], e)
        countI += 1
    print(wLArray)
    wLArray.shape
    
    almArray = []
    lCounter = 0
    while lCounter < 1025:
        mCounter = 0
        mMax = lCounter+1
        print("We are at l = ", lCounter)
        while mCounter < mMax:
            almList = np.asarray([sph_map_array[0][mCounter], sph_map_array[1][mCounter], sph_map_array[2][mCounter], sph_map_array[3][mCounter], sph_map_array[4][mCounter], sph_map_array[5][mCounter], sph_map_array[6][mCounter]])
            newAlm = almList.T@wLArray[:,lCounter]
            almArray.append(newAlm)
            mCounter += 1
        lCounter += 1
    
    npALM = np.asarray(almArray)
    new_sph_map = hp.sphtfunc.alm2map(npALM, nside = 1024,lmax = 1024)
    
    return new_sph_map


new_sph_map = processMapsSpherical(map_array_old)
hp.mollview(new_sph_map, nest=False, norm='hist')

