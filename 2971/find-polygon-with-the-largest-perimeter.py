# 如果 nums[i] 是小棒子的長度，問「能用棒子組出的多邊形」週長
# 其實只有1條規則： 小棒子加起來的總長度，要比大的棒子長。
# 所以把 nums.sort() 排好後，從小到大，逐一加到總長度中
# 並時時測「比大棒子長」，便能更新 ans
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort() # 從小到大排好

        ans = -1 # 如果找不到答案，return -1
        now = nums[0] + nums[1] # 先從三角形開始測，準備2個邊
        for num in nums[2:]: # 要（逐一）加入新的邊
            if now>num: # 總長比較長，就是合法的多邊形週長
                ans = now+num # 更新ans
            now += num # 總長又變長了
        return ans
