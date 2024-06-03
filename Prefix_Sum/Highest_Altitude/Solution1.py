class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maxAltitude = 0
        currAltitude = 0

        for change in gain:
            currAltitude += change
            maxAltitude = max(maxAltitude, currAltitude)
        
        return maxAltitude