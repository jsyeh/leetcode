# 螞蟻讀入 nums[i] 後，會往左 or 往右走。
# 問它「回到原本boundary」幾次
class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        ant = 0 # ant 所在位置
        ans = 0
        for num in nums:
            ant += num # ant 照著nums[i] 走到下一個位置
            if ant==0: ans += 1 # 若回到 0 答案就多一次
        return ans
