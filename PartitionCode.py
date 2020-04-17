import numpy as np
import healpy as hp

#Linear algebra approach

def get_H(map_array):
    '''
    Returns the matrix H necessary for the linear algebra approach
    as outlined in the lecture notes.
    Params:
    -------
    map_array: An array of healpix maps that we will be fitting
               the linear function to
    Returns:
    --------
    H: Two dimensional array, outlined as it was in the lecture notes
    '''
    i = 0
    j = 0
    H = np.zeros((len(map_array), len(map_array)))
    
    for m in map_array:
        
        j = 0
        for n in map_array:
            product = m*n
            product_sum = np.sum(product)
            H[i, j] = product_sum
            j+=1
        i+=1
    return H

def sliceFixer(num_slices,array_maps):
    '''
    Slices up the map into different regions
    Params:
    -------
    num_slices: Int, number of slices of the map that are requested
    array_maps: An array of maps, contatins all the maps that we wish to make
                a linear combination of
    Returns:
    --------
    slicedUpMaps: an array containing each map in array_maps, in sliced up form
                  array has form [slices,map,mapinfo]

    '''
    

    length_maps = len(array_maps[0])
    slicedUpMaps = []

    #Error catching
    if not (length_maps%num_slices == 0 ):
         raise TypeError('length_maps%num_slices != 0, cannot slice maps')


    #Start for the slices
    lowerBound = 0
    upperBound = int(length_maps/num_slices)
    
    for i in range(num_slices):   #Goes over the number of slices
        mapSlicesToAdd = []        
        for j in array_maps:
            #Slices the data, and appends it to the 'to add' array
            mapSlicesToAdd.append(j[lowerBound:upperBound])
        slicedUpMaps.append(mapSlicesToAdd)  #Add the map slices

        lowerBound = upperBound
        upperBound += int(length_maps/num_slices)
    return slicedUpMaps
        
def slicedWeightGetter(mapSlice_array):
    '''
    returns the weight for a given slice
    Params
    ------
    mapSlice_array: a slice of a given portion of the sky over all the maps we are normalizing over
    
    Returns
    -------
    w = Array of weights for the map
    '''
    #Get s
    H = get_H(mapSlice_array)
    e = np.ones(len(mapSlice_array))
    
    w = (np.linalg.inv(H)@e) / (e.T@H@e)
    w = w/np.sum(w)  #apply the constraint all the weights must equal 1
    
    return w

def sliceCMBFixer(num_slices,map_array):
    '''
    This method will implement the slicing method to improve CMB foreground removal based on the assumption that
    the CMB acts as a blackbody
    Params
    ------
    num_slices: the number of slices we are taking of the map
    map_array: the array of maps at different frequencies of the CMB
    
    Returns
    -------
    fixed_map: the map that has had the foreground cleared using the slicing method
    
    

    '''
    #Slice up the cmb into different maps
    slicedMap = sliceFixer(num_slices, array_maps=map_array)
    
    #Apply linear algebra method (seen in class) to each map
    weights = []  #array of weights corresponding to each slice
    for i in range(num_slices):
        weights.append(slicedWeightGetter(slicedMap[i]))
    weights = np.asarray(weights)
    #Recombine the slices with the new weights
    fixed_map = []
    for i in range(num_slices):
        currentSlice = slicedMap[i]
        currentSlice = np.asarray(currentSlice)
        fixedPortion = weights[i]@currentSlice
        fixed_map.append(fixedPortion)
    #convert to a numpy array and flatten
    fixed_map = np.asarray(fixed_map).flatten()
    return fixed_map
    
    
        
        