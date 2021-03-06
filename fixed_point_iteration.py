    
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 00:25:14 2019
@author: Abdulkadir Kahraman
"""


import numpy as np


"""
%Program 1.2 Fixed-Point Iteration
%Computes approximate solution of g(x)=x
%Input: function handle g, starting guess x0,
%       number of iteration steps k
%Output: Approximate solution xc
"""
def fixedpoint(f,x0,tol=10**-8,maxiter=100):
 e = 1
 itr = 0
 xp = []
 r=-0.9708989225662239
 while(e > tol and itr < maxiter):
  x = f(x0)      # fixed point equation
  print (itr, x0, x, abs(x-r),abs(x-r)/x0 )
  e = (x0-x) # error at the current step
  x0 = x
  xp.append(x0)  # save the solution of the current step
  itr = itr + 1
 print (itr, x0, x)
 return x,xp
 
# Sample functions for test 
#f = lambda x: (sin(x)-5)/6
#f = lambda x: x**2+x/2-1/2
#f = lambda x: x**(1/2)
f = lambda x: (np.sin(x)-5)/6

# Test the bisection method
x_start = 0
x_final,x_points = fixedpoint(f,x_start)
