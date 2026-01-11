# LeetCode 1318. Minimum Flips to Make a OR b Equal to c
class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        ans = 0
        while a or b or c:
            if (a%2 or b%2) != c%2:
                if c%2==0: ans += a%2 + b%2
                else: ans += 1
            a, b, c = a//2, b//2, c//2
        return ans
