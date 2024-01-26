# nums 裡挑2個數，它們「最大的位數」「相同」
# 找「最起來」最大
# 總共只有 100個數，可用暴力法
class Solution:
    def maxSum(self, nums: List[int]) -> int:
        def maxDigit(n): 
            ans = 0
            while n>0: # 剝皮法，找最大的數
                ans = max(ans, n%10)
                n //= 10
            return ans

        group = defaultdict(list)
        for num in nums: # 依照最大的數，分群
            group[maxDigit(num)].append(num)

        ans = -1
        for digit in group: # 針對每一個數
            if len(group[digit])<2: continue # 不夠取
            group[digit].sort(reverse=True) # 反著排序
            ans = max(ans, group[digit][0]+group[digit][1]) # 挑最大的2個數，相乘後更新答案
        return ans
