# -*- coding: utf-8 -*-
"""
Created on Sat May 21 17:08:19 2016

@author: vishen
"""

import numpy as np
import matplotlib as plot
import pylab
#### example with 7 CR images
#### X_train.shape = (7,3,224,224) 

X1 = X2 = X3 = X4 = np.zeros((7,1,112,112))
for i in range(224) :
    for j in range(224):
        
        if np.mod(i,2) == 1 and np.mod(j,2) == 1:    
            X1[:,0,i/2 ,j/2 ] = X_train[:,0,i,j]
            
        elif np.mod(i,2) == 1 and np.mod(j,2) == 0:
            X2[:,0,i/2 ,j/2] = X_train[:,0,i,j]
            
        elif np.mod(i,2) == 0 and np.mod(j,2) == 1:
            X3[:,0,i/2 ,j/2] = X_train[:,0,i,j]
            
        else:
            X4[:,0,i/2 ,j/2] = X_train[:,0,i,j]

pylab.imshow(X_train[0,0,:], cmap=pylab.cm.bone)
pylab.imshow(X1[0,0,:], cmap=pylab.cm.bone)
pylab.imshow(X2[0,0,:], cmap=pylab.cm.bone)
pylab.imshow(X3[0,0,:], cmap=pylab.cm.bone)


pylab.imshow(X_train[1,1,:], cmap=pylab.cm.bone)
pylab.imshow(X1[1,0,:], cmap=pylab.cm.bone)

####  decomposing an array by half&half; 
####  assuming input array having shape(nb of images,1 channel, length, width)
def decompose_image (X_train):
    nb_images = X_train.shape[0]
    length = X_train.shape[2]
    X = np.zeros((nb_images,4,length/2,length/2))
    for i in range(length):
        for j in range(length):
            
            if np.mod(i,2) == 1 and np.mod(j,2) == 1:
                X[:,0,i/2,j/2] = X_train[:,0,i,j]
                
            elif np.mod(i,2) == 1 and np.mod(j,2) == 0:
                X[:,1,i/2,j/2] = X_train[:,0,i,j]
                
            elif np.mod(i,2) == 0 and np.mod(j,2) == 1:
                X[:,2,i/2,j/2] = X_train[:,0,i,j]
            else:
                X[:,3,i/2,j/2] = X_train[:,0,i,j]
    return X
    
    
    
####
    
    
    
    
    
    
    
    