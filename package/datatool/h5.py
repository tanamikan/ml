# import module
import h5py
import numpy as np
import matplotlib.pyplot as plt
import cv2
from glob import glob
import os

            
            
# hdf5ファイルの作成
def hdf5_generate(file_path):
    f = h5py.File('file.hdf5', mode='w')
    group = f.create_group('/images')
    file_list = glob(file_path)
    
    for file in file_list:
        arr = cv2.imread(file)
        dataset = group.create_dataset(name = os.path.basename(file), shape=arr.shape, dtype=np.uint8)
        dataset[...] = arr
        
    f.close()