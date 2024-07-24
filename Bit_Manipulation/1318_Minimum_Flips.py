# Given 3 positives numbers a, b and c. Return the minimum flips required in
# some bits of a and b to make ( a OR b == c ). (bitwise OR operation). Flip
# operation consists of change any single bit 1 to 0 or change the bit 0 to 1 in
# their binary representation.

class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        flips = 0
        while a > 0 or b > 0 or c > 0:
            bit_a = a & 1
            bit_b = b & 1
            bit_c = c & 1

            if bit_c == 0:
                flips += (bit_a + bit_b)  
            else:
                if bit_a == 0 and bit_b == 0:
                    flips += 1  

            a >>= 1
            b >>= 1
            c >>= 1

        return flips