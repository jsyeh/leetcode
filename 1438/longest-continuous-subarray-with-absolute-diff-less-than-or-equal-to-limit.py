# LeetCode 1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
# 從「左邊尾巴i 連續到 右邊頭j」的subarry裡，最大值-最小值<=limit 的條件下，找最長的長度
# 又是sliding window 像「毛毛蟲」一樣伸縮，以符合條件
# 但是要怎麼「快速」找到「最大值」「最小值」呢？可利用 mono queue 來做。（這題應該算是 Hard 題）
# 去年我寫 239. Sliding Window Maximum (Hard) 用 deque 的方法可拿來用
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxq, minq = deque(), deque()  # 用來存 mono queue
        i = 0  # 對應左邊的尾巴
        for num in nums:  # 逐一取出數字，對應右邊的頭
            while len(maxq)>0 and num > maxq[-1]: # 頭的數字要壓入 maxd 前
                maxq.pop() # 要先把queue裡較小的數，都清掉
            maxq.append(num) # 才能壓入，並保持 mono queue 的大小順序（大到小）
            while len(minq)>0 and num < minq[-1]: # 頭的數字要壓入 mind 前
                minq.pop()  # 要把queue裡較大的數，都清掉
            minq.append(num) # 才能壓入，並保持 mono queue 的大小順序（小到大）
            if maxq[0] - minq[0] > limit:  # 超過範圍，要吐出來，尾巴要變短
                # 要吐出左邊尾巴i對應的數字（如果它還在 mono queue 裡的話）
                if maxq[0]==nums[i]: maxq.popleft()
                if minq[0]==nums[i]: minq.popleft()
                i += 1  # 尾巴往右移
        return len(nums) - i

