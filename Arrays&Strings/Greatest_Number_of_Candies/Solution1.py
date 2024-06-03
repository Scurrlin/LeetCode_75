class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        n = len(candies)
        maximum = max(candies)
        result = []
        for i in range(n):
            if candies[i] + extraCandies >= maximum:
                result.append(True)
            else:
                result.append(False)
        return result