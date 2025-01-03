# LeetCode 66. Plus One
# 把 digits 對應的數 +1，不過要小心「進位」的問題，位數可能會多1位
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        N = len(digits)
        carry = 1
        for i in range(N-1, -1, -1):
            digits[i] += carry
            carry = digits[i] // 10
            digits[i] %= 10
        if carry==0: return digits  # 最後沒有進位
        return [carry] + digits  # 最後還有進位，放在更前面
