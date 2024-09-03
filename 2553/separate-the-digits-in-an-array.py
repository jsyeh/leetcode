# LeetCode 2553. Separate the Digits in an Array
# 把把數字的每一位數，分開後，再塞進 list 裡
class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            for d in str(num):  # 轉換成字串，就能「逐位」取出來
                ans.append(int(d))  # 再轉回數字，塞入答案裡
        return ans
