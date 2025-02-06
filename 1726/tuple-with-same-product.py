# LeetCode 1726. Tuple with Same Product
# nums 的數都不同，找 4 個數 a*b==c*d（可調順序）有幾組？
# 題目 Hint 1 暴力試2數相乘， Hint 2 用排列組合來找答案，
# 但我想不出來。看了 Ye Gao 的解法，還真的這樣做
class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        ans = 0
        counter = Counter()
        N = len(nums)  # 陣列長度
        for i in range(N):  # 左手 i Hint 1 暴力試2數相乘
            for j in range(i+1,N):  # 右手 j，把各種乘法的可能，都做一次
                now = nums[i] * nums[j]  # c*d
                # Hint 2 用排列組合來找答案
                ans += counter[now]  # 現在 c*d ，之前 a*b 出現過幾次，就加幾組
                counter[now] += 1  # 現在再加1組 a*b
        return ans * 8  # 真強！這個想法，是左右各2個數
        # 交換、交換，再「左右大交換」2*2*2=8 
