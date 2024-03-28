# 想找最長的 subarray 且裡面「重覆的數」不能超過K次
# 應該還是可以用「毛毛蟲」的做法, two pointers來找答案
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        left = right = 0
        ans = 0
        counter = Counter()
        for right in range(len(nums)): # 毛毛蟲右邊的頭
            now = nums[right] # 現在吃到的數
            counter[now] += 1
            while counter[now] > k: # 不合格、需要左邊的尾巴右縮, 直到合格為止
                counter[nums[left]] -= 1
                left += 1
            ans = max(ans, right-left+1) # 更新答案
        return ans
