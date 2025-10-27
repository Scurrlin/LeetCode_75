# Given a string containing digits from 2-9 inclusive, return all possible
# letter combinations that the number could represent. Return the answer in any
# order.

# A mapping of digits to letters (just like on the telephone buttons) is given
# below. Note that 1 does not map to any letters.

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d, res = digits, []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(i, currStr):
            if len(currStr) == len(d):
                res.append(currStr)
                return
            for c in digitToChar[d[i]]:
                backtrack(i + 1, currStr + c)

        if d:
            backtrack(0, "")
        return res