# LeetCode 1695. Maximum Erasure Value
# nums 陣列裡，將「一段連續、數值都不同」的subarray消掉，最多能消多少？
# 看起來就用伸縮自如的「毛毛蟲」two pointers 就可解了
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        tail = head = 0  # 「毛毛蟲」左邊尾巴、右邊頭
        subarray = set()  # 「毛毛蟲」目前體內有哪些數
        ans = now = 0  # 最後答案ans、目前的值now
        while head < len(nums):  # 「毛毛蟲」右邊頭「還沒超過邊界」，將要吃 nums[head]
            while nums[head] in subarray:  # 「毛毛蟲」體內已有nums[head]
                subarray.remove(nums[tail])  # 「毛毛蟲」尾巴就一直吐到乾淨
                now -= nums[tail]  # 「毛毛蟲」目前體內總和的值 變少、瘦身
                tail += 1  # 「毛毛蟲」尾巴右移
            # 「毛毛蟲」把尾巴吐乾淨後，便能吃東西囉！
            subarray.add(nums[head])  # 「毛毛蟲」放心的把 nums[head] 吃進去
            now += nums[head]  # 「毛毛蟲」目前分數增加
            ans = max(ans, now)  # 更新答案、找到最大值
            head += 1  # 「毛毛蟲」頭往右一格，等待下一輪的變化
        return ans
