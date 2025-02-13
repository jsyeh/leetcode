# LeetCode 3066. Minimum Operations to Exceed Threshold Value II
# nums 每次挑最小的2個數x,y去除，再於任意處加入 min(x,y)*2+max(x,y)
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapify(nums)  # 把陣列 nums 「轉換成heap資料結構」
        ans = 0  # 要做幾次，才能將 nums 裡，全部的數都 >= k 呢？
        while nums and nums[0]<k:  # 還有剩數字，且「最小數」還不夠小
            x, y = heappop(nums), heappop(nums)  # 吐出2個最小的數
            heappush(nums, min(x,y)*2+max(x,y))
            ans += 1
        return ans
