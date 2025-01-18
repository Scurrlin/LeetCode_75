# You are given two positive integer arrays spells and potions, of length n and
# m respectively, where spells[i] represents the strength of the ith spell and
# potions[j] represents the strength of the jth potion.

# You are also given an integer success. A spell and potion pair is considered
# successful if the product of their strengths is at least success.

# Return an integer array pairs of length n where pairs[i] is the number of
# potions that will form a successful pair with the ith spell.

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        pairs = []
        s, p = spells, potions
        p.sort()
        n = len(p)

        for i in range(len(s)):
            l, r = 0, len(p) - 1
            
            while l <= r:
                m = (l + r) // 2
                if s[i] * p[m] >= success:
                    r = m - 1
                else:
                    l = m + 1
            if l < len(p):
                pairs.append(n - l)
            else:
                pairs.append(0)

        return pairs