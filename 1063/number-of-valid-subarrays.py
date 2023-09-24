# 找 valid subarrays 的數量，即「最左邊是最小」的subarray
# 參考Editorial 的解法，使用 Monotonic Stack
# 解題策略：有個stack裡面會放「最左邊最小」的各式開始index
#（stack會對應「單調遞增數列」的index）
# 裡面存「右邊下一個遞增的數」的index
class Solution:
    def validSubarrays(self, nums: List[int]) -> int:
        ans = 0
        stack = [] # 放「從小到大」對應的index
        for i in range(len(nums)):
            # 每個nums[i]都可能是「最左邊最小」的開始
            while len(stack)>0 and nums[i]<nums[stack[-1]]: 
                # 若新數字更小（無法繼續加大stack）
                ans += (i-stack[-1]) # 先更新ans（回補）
                stack.pop() # 再拔掉stack top
                # print(stack)
            # 因前面拔光大的，現在nums[i]夠大，可塞入 i
            stack.append(i) 
            # print(stack)
        # print("===")
        while len(stack)>0:
            ans += len(nums) - stack[-1] # （回補）
            stack.pop()
            # print(stack)
        return ans

