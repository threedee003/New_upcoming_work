
"""
These are some image augmenting functions. 

"""


import numpy as np
import matplotlib.pyplot as plt
import os
import skimage.io as io
import warnings





def transposer(img):                  # image has to have equal height and width.
    h, w, n = img.shape[0], img.shape[1], img.shape[2]
    if h != w:
        print("The image is not square and cannot be transposed")
        return img.astype(img.dtype)
    for i in range(n):
        img[:,:,i] = np.transpose(img[:,:,i])
    return img.astype(img.dtype)
    


def rotate(img,k):
    n = img.shape[2]
    dt = img.dtype
    for i in range(n):
        img[:,:,i] = np.rot90(img[:,:,i],k,axes = (0,1))
    return img.astype(dt)



def data_rotate(src_f,save_path,P):
    for f in os.listdir(src_f):
        img_ = io.imread(os.path.join(src_f,f),plugin='matplotlib')
        img_ = rotate(img_,P)
        io.imsave(f'{save_path}\\{f}',img_)
    print("Data has been augmented and has been rotated {} times".format(P))