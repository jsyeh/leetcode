# 可任意挑 startValue，加上 nums[i] 過程中，每次得到的值都「不會比1小」
# 希望 startValue 是最小的正整數
# 所以其實就是「先拿任一個數」(ex. 1)開始，看它的「最小值」後，再往上撐上去即可
class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        ans = lowest = now = 1 # 先挑1 當預設答案
        for num in nums: # 每個數字，逐項加加看
            now += num
            lowest = min(lowest, now) # 同時記錄最低值
        if lowest<1: # 太低的話，要往上抬昇，使得 lowest 值抬到1以上
            ans += -lowest + 1 # 目前 lowest-1<0, 所以要要 -(lowest-1) 負負得正
        return ans
