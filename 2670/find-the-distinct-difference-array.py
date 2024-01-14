# 左邊有幾個、右邊有幾個（不同的數)，再相減
# 看題目， [i] 的部分，左包含、右不包含哦！
class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        N = len(nums) # 長度
        prefix = [0]*N # 左邊有幾個不同的
        suffix = [0]*N # 右邊有幾個不同的
        left = set() # 利用 set()來知道「有幾個不同」
        right = set()
        for i,num in enumerate(nums):
            left.add(num) # 左到右
            prefix[i] = len(left)
        for i in range(N-1,-1,-1): # 右到左
            suffix[i] = len(right) # 右不包含，調一下
            right.add(nums[i])
        ans = [0]*N
        for i in range(N): # 照公式，算出答案
            ans[i] = prefix[i]-suffix[i]
        return ans
