# We are playing the Guess Game. The game is as follows:

# I pick a number from 1 to n. You have to guess which number I picked.

# Every time you guess wrong, I will tell you whether the number I picked is
# higher or lower than your guess.

# You call a pre-defined API int guess(int num), which returns three possible
# results:

# -1: Your guess is higher than the number I picked (i.e. num > pick). 1: Your
# guess is lower than the number I picked (i.e. num < pick). 0: your guess is
# equal to the number I picked (i.e. num == pick). Return the number that I
# picked.

class Solution:
    def guessNumber(self, n: int) -> int:
        low, high = 1, n
        while (res := guess(mid := ((high + low) >> 1))) != 0:
            if res == -1: high = mid - 1
            else: low = mid + 1
        return mid