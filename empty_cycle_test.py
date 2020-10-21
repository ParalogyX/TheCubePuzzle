# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 15:26:08 2020

@author: vpe
"""
import time

count = 0
start = time.time()       
for i in range (int(1E9)):
    count += 1
end = time.time()
print("Empty sycle (1E9): ", end - start)
print (i)