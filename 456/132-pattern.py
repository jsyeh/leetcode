# 132 pattern 是 低、高、中 的順序。
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        N = len(nums)
        left = [0]*N # 裡面會存 left裡面最小的值
        left[0] = nums[0]
        for j in range(1,N):
            left[j] = min(left[j-1], nums[j]) # 可查「之前最小值」

        stack = []
        for j in range(N-1, -1, -1): # 中間的數字
            while len(stack)>0 and nums[j] > stack[-1]:
                if left[j] < stack[-1]: # stack[-1]對應右邊數字
                    return True # 符合 132 低高中 的順序
                stack.pop() # mono stack 是單調遞增，所以nums[j]>stack[-1]，刪
            stack.append(nums[j]) # mono stack 再把新的數字加進去
        return False
