# LeetCode 1318. Minimum Flips to Make a OR b Equal to c
class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        ans = 0
        while a>0 or b>0 or c>0:
            a0, b0, c0 = a%2, b%2, c%2
            if a0==0 and b0==0 and c0==1: ans += 1
            elif c0==0:
                if a0==1: ans += 1
                if b0==1: ans += 1
            a, b, c = a//2, b//2, c//2
        return ans
