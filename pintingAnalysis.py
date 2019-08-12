# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 09:06:53 2019

@author: Sagi
"""
import numpy as np
from matplotlib import pyplot as plt
import math 

def normalize(v):
    norm = np.linalg.norm(v)
    if norm == 0: 
       return v
    return v / norm

def getUnitVec(v,v0): 
    v = np.mat(v)
    v0 = np.mat(v0)
    v_tmp = v-v0
    a = normalize(v_tmp)
    return a

def getBeamDirection(filename,filepath='C:\\Users\\Sagi\\Desktop\\G-Clef\\injectionOptics\\InjectionPrototype\\Test5\\'):
    beam_direction = []
    with open(filepath+filename) as fp:
        line = fp.readline()
        data = str.split(line)
        v0 = [float(data[1])*3.5e-3, float(data[2])*3.5e-3 ,float(data[0])]
        line = fp.readline()
        while line:
            data = str.split(line)
            v = [float(data[1])*3.5e-3, float(data[2])*3.5e-3 ,float(data[0])]
            norm_a = getUnitVec(v,v0)  
            beam_direction.append(norm_a)
            line = fp.readline()
            x,y,z = [],[],[]
            for unit_vec in beam_direction:
                x.append(unit_vec[0,0])
                y.append(unit_vec[0,1])
                z.append(unit_vec[0,2])
                direction =[np.mean(x),np.mean(y),np.mean(z)]
                return direction


file_names  = ['Test5_Fiber5.txt','Test5_Fiber6.txt','Test5_Fiber7.txt','Test5_Fiber8.txt']
fibers = []
angles = []

for fn in file_names:    
    fibers.append(getBeamDirection(fn))

for i in range(0,len(fibers)):
    v0 = np.mat(fibers[1])
    v_tmp = np.mat(fibers[i])
    angles.append(math.degrees(math.acos(np.dot(v0,np.transpose(v_tmp)))))


print(angles)
print(np.std(angles))
#v0 = np.mat([1144.9069*3.5e-3, 1129.8657*3.5e-3, 0])
#v_coords = np.mat([1124.9535*3.5e-3, 1141.8378*3.5e-3, 4])
#
#for vec in v_coords:
#    v_tmp = vec-v0
#    b = normalize(v_tmp)
#
#
#print(a)
#print(b)
#
##print(np.dot(a,b))
#angle = math.degrees(math.acos(np.dot(a,np.transpose(b))))
#print(angle)   