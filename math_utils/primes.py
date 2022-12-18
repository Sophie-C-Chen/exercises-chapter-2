"""Determines whether an integer input is prime."""
from math import sqrt

def isprime(n):
   # check input is greater than zero
   if n >= 2:
      # Calculate square root of n and take only integer part, m
      sqroot = int(sqrt(n))
      #return sqrootquit

      # If m is divisible by any integer less than m, then it is non-prim; else, it is prime.
      for i in range(sqroot-1):
         if n % (i+2) == 0: 
            return False
         i+=1
      return True
   # input is invalid, 0, or 1
   return False
      
         
