class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        freq1 = [0] * 26
        freq2 = [0] * 26

        for ch in word1:
            freq1[ord(ch) - ord('a')] += 1
        for ch in word2:
            freq2[ord(ch) - ord('a')] += 1

        for f1, f2 in zip(freq1, freq2):
            if (f1 == 0) != (f2 == 0):
                return False

        return sorted(freq1) == sorted(freq2)