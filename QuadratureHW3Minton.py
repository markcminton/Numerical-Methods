 #     a. PROGRAMMER: Mark Minton

 #     b. COURSE:    CSCI 3231   (section #2)

 #     c. DATE:    January 27, 2020

 #     d. ASSIGNMENT:   Number 3

 #     e. ENVIRONMENT: Windows 10 Python

 #     f. FILES INCLUDED: .py file 

 #     g. PURPOSE:  Use Estimated Integral (Quadrature) to find area under of a curve

 #     h. INPUT:  Equations and Quadrature Integral

 #     i. PRECONDITIONS:    Assumptions for correct execution of this code

 #     j. OUTPUT:  Estimated Area and Error of Estimate

 #     k. POSTCONDITIONS: Assertions that describe the results of actions taken by code

 #     l. ALGORITHM:  Quadrature using scipy library

 #     m.  ERRORS:   6.482072250655975e-15)
 #                   4.31390266082868e-15)
#                    5.640647112820812e-14
 #     n.  EXAMPLE: N: 9 = 2.218972210137635
                    #|f(x)| =  2.220446049250313e-16
                    #Good Result


 #     o.  HISTORY: https://docs.scipy.org/doc/scipy/reference/integrate.html







import math
from math import e
import numpy as np 
import scipy
import scipy.integrate
from scipy.integrate import quad #scipy intergration 

def f1(x): # f(x) #1
    return (1 - math.sin((1-x)))

def f2(x): # f(x) #2
    return (math.sqrt(x+1)+1)

def f3(x): # f(x) #3
    return (math.tanh(x+1))   
    

def main():
   result1 = quad(f1,-1,1) #quadratures
   result2 = quad(f2,-1,1)
   result3 = quad(f3,-1,1)

   print ("Estimated Area over Function 1 and Error:", result1)
   print ("Estimated Area over Function 2 and Error:", result2)
   print ("Estimated Area over Function 3 and Error:", result3)


if __name__ == '__main__':
    main()