 #     a. PROGRAMMER: Mark Minton

 #     b. COURSE:    CSCI 3231   (section #2)

 #     c. DATE:    January 27, 2020

 #     d. ASSIGNMENT:   Number 1

 #     e. ENVIRONMENT: Windows 10 Python

 #     f. FILES INCLUDED: .py file 

 #     g. PURPOSE: Demonstrate rounding errors of a computing system

 #     h. INPUT:  Equations and n number of h's

 #     i. PRECONDITIONS:    -26.64510337034830854

 #     j. OUTPUT:  Approximation of derivative at 2 radians

 #     k. POSTCONDITIONS: ############################

 #     l. ALGORITHM:  Given formulas

 #     m.  ERRORS:   example of error: Error = -3.823121419088693e-05

 #     n.  EXAMPLE:  h =  3.637978807091713e-12 Result = -26.6451416015625 Error = -3.823121419088693e-05


 #     o.  HISTORY: ########################


import math 
import numpy as np
from math import e
def function(x):
	result = (math.sin(x**4) + (x**2))
	return result

def main():

	x = 2.0
	h = 1

	while h > (0.000000000002):

		h = h/2

		fprimex = ((function(x+h) - function(x)) / h)

		print (" h = ",h, "Result =",fprimex, "Error =", fprimex - (4 + (32*math.cos(16))))
   	 
	 	
	print ("True Answer:",(4 + (32*math.cos(16))))


if __name__ == '__main__':
	main()    
	