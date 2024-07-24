# For two strings s and t, we say "t divides s" if and only if s = t + t + t +
# ... + t + t (i.e., t is concatenated with itself one or more times).

# Given two strings str1 and str2, return the largest string x such that x
# divides both str1 and str2.

from math import gcd

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""

        gcd_length = gcd(len(str1), len(str2))
        gcd_str = str1[:gcd_length]

        str1_check = str1 == gcd_str * (len(str1) // len(gcd_str))
        str2_check = str2 == gcd_str * (len(str2) // len(gcd_str))

        if str1_check and str2_check:
            return gcd_str

        return ""