# data-final

The dataset used is all of the full mission maps up to 353 GHz from the Planck mission available at https://irsa.ipac.caltech.edu/data/Planck/release_2/all-sky-maps/.

## setting up

The data shown in our report are generated in `CMB_Map.ipynb` using data from the link above. The exact data sets needed are 

## organization

The data are stored in a folder outside of the `/data-final` directory called `data_files`.

## files for submission

The following are the files which are to be considered as our final submission.

### CMB_Foreground_Removal.pdf

This is the final report.

### CMB_Map.ipynb

This notebook generates all of the maps included within our report.

### tests

This folder contains two files, `tests_PartitionCode.py` and `test_SphericalCode.py`, the first containing test functions for the partition method and the second containing tests functions for the spherical harmonics method.

### PartitionCode.py

This file contains the functions used in the partition method. Functions from this file are imported and called in `CMB_Map.ipynb`.

### SphericalCode.py

This file contains the functions used in the spherical harmonics method. Functions from this file are imported and called in `CMB_Map.ipynb`.

