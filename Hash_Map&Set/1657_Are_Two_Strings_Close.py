# Two strings are considered close if you can attain one from the other using
# the following operations:

# Operation 1: Swap any two existing characters. For example, abcde -> aecdb
# Operation 2: Transform every occurrence of one existing character into another
# existing character, and do the same with the other character. For example,
# aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)

# You can use the operations on either string as many times as necessary.

# Given two strings, word1 and word2, return true if word1 and word2 are close,
# and false otherwise.

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