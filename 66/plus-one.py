# LeetCode 66. Plus One
# 把 digits 對應的數 +1，不過要小心「進位」的問題，位數可能會多1位
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ans, carry = 0, 1  # 把「要加1」的1藏在carry裡
        for i in range(len(digits)-1, -1, -1):  # 反過來的迴圈
            carry += digits[i]  # 現在這個位數的加總
            carry, digits[i] = carry//10, carry%10  # 進位、留在原位
        if carry>0: return [1] + digits  # 若最後還有進位，就加長1格
        return digits  # 沒額外進位，直接回傳答案
