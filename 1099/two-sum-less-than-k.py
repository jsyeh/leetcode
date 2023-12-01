# 想要找 nums[i] + nums[k] < k 且最大的值
# 直覺覺得 sort() 後，用 2 pointer 的方法，左右來找最大值
class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort() # 從小到大排好

        ans = -1 # 預設的答案
        i, j = 0, len(nums)-1 # 左邊界、右邊界
        while i<j: # 只要邊界還沒撞在一起，就繼續測試
            if nums[i] + nums[j]>=k: # 太大，超過範圍
                j-=1 # 太大的話，j要左移
            else: # 合理的值
                ans = max(ans, nums[i]+nums[j])# 有更好的答案
                i+=1 # 因還能接受的大小，再試大一點看看
        
        return ans
# case 54/125: 小心 nums[i] + nums[j] 要 < k 不能等於k
