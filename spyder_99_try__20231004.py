# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
k=0
for i in range(1,10):
    for j in range(1,10):
        k=i*j
        print("%d * %d = %2d  " %(j,i,k),end="")
    print()