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