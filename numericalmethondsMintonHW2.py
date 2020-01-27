 #     a. PROGRAMMER: Mark Minton
 #     b. COURSE:    CSCI 3231   (section #2)

 #     c. DATE:    January 27, 2020

 #     d. ASSIGNMENT:   Number 2

 #     e. ENVIRONMENT: Windows 10 Python

 #     f. FILES INCLUDED: .py file 

 #     g. PURPOSE:  Find zeros of equations with secand method

 #     h. INPUT:  Equations and two guesses (recusive guesses) total of 10 guesses

 #     i. PRECONDITIONS:    True answer is about 2.21897221013763458

 #     j. OUTPUT:  New guesses/zeros

 #     k. POSTCONDITIONS: #####################
 
 #     l. ALGORITHM:  Recusive Secant Method

 #     m.  ERRORS:  #############

 #     n.  EXAMPLE: N: 9 = 2.218972210137635
                    #|f(x)| =  2.220446049250313e-16
                    #Good Result


 #     o.  HISTORY: https://en.wikipedia.org/wiki/Secant_method


import math
from math import e
import numpy as np 

def function(x): # f(x)
    return (math.cos((x**2/4.0)) - (1.0/3.0))
    # = 0 ?

def secant (x1,x2): # secant function
    return ((x2*function(x1)-(x1*function(x2)))/(function(x1)-function(x2)))


def main():
    #secand method using 2 intial guesses
    guess1 = 2
    guess2 = 3

    #init secent 
    
    print ("N:",1,"=", secant(guess1,guess2))
    print ("|f(x)| = ",abs(function(secant(guess1,guess2))))

    # new root xn
    guess1 = secant(guess1,guess2)
    
    for x in range(1,9,1): # 10ish guesses

        if x%2 == 0: # to alternate geusses, this case is even so second guess (recusive)
            print ("N:",x+1,"=", secant(guess1,guess2))
            guess2 = secant(guess1,guess2)
            print ("|f(x)| = ",abs(function(secant(guess1,guess2))))
            if abs(function(secant(guess1,guess2))) < 0.000000001: # check if good result
                print ("Good Result")
        else: # odd guess one 
            print ("N:",x+1,"=", secant(guess1,guess2))
            guess1 = secant(guess1,guess2)
            print ("|f(x)| = ",abs(function(secant(guess1,guess2))))
            if abs(function(secant(guess1,guess2))) < 0.000000001: # check if good result
                print ("Good Result")
        


if __name__ == '__main__':
    main()