# The Tribonacci sequence Tn is defined as follows: 

# T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

# Given n, return the value of Tn.

class Solution:
    def tribonacci(self, n: int) -> int:

        t0 =0
        t1= 1
        t2 =1
        for i in range(n):
            temp = t0
            t0 = t1
            t1 = t2
            t2 = temp + t0 + t1
            
        return t0