# LeetCode 3340. Check Balanced String
# 確認一下 num 字串裡「奇數位相加 == 偶數位相加」
class Solution:
    def isBalanced(self, num: str) -> bool:
        odd = even = 0  # 奇數位、偶數位，各自加到 odd 和 even 裡
        for i, digit in enumerate(num):  # 用迴圈，逐一檢查
            if i%2==0: even += int(digit)  # 偶數位，加到 even 裡
            else: odd += int(digit)  # 奇數位，加到 odd 裡
        return odd == even  # 看是否「奇數位相加 == 偶數位相加」
