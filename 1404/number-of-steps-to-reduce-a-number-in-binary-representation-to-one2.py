# LeetCode 1404. Number of Steps to Reduce a Number in Binary Representation to One
# 偶數//2, 奇數+1 問什麼時候變1
class Solution:
    def numSteps(self, s: str) -> int:
        ans = 0  # 總共要走幾步
        n = int(s, 2)  # 把字串 s 當二進位整數變成 n
        while n > 1:  # 目標:n最後會變成1
            if n%2==0: n = n // 2  # 偶數//2
            else: n = n + 1  # 奇數+1
            ans += 1  # 又多做了一步哦!
        return ans  # 總共要走幾步
