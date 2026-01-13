# LeetCode 374. Guess Number Higher or Lower
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

# LeetCode 374. Guess Number Higher or Lower
class Solution:
    def guessNumber(self, n: int) -> int:
        return bisect_left(range(n+1), 0, key=lambda x: -guess(x))
