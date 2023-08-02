# 因為是圓形，所以頭尾要考量
# 剛好 Python 的陣列，如果超過的話，就是 Circular 所以可能更容易解
# 不過想到 table 不夠用，應該分成 table0[i] 及 table1[i]
# 對應：包含0及i的最大值、包含1及i的最大值，分開記錄
class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        if N == 1: # 只有1戶，搶它
            return nums[0]
        if N == 2: # 只有2戶，搶多錢的
            return max(nums[0], nums[1])
        if N == 3: # 只有3戶，搶多錢的那一戶，因為另2戶必相鄰
            return max(nums[0], nums[1], nums[2])

        # 再來是4戶以上囉
        table0 = [0]*N # 包含nums[0]的最佳解
        table1 = [0]*N # 不包含 nums[0] 的最佳解
        table0[0] = nums[0] # table[i]表示有挑選 nums[i] 的最佳解
        table1[1] = nums[1]
        table0[2] = table0[0] + nums[2]
        table1[2] = nums[2] # 小心這個，別漏了
        # 再來是4戶以上囉
        
        for i in range(3,N):
            table0[i] = nums[i] + max(table0[i-2], table0[i-3])
            table1[i] = nums[i] + max(table1[i-2], table1[i-3])
            # 包含0及i的最大值、包含1及i的最大值，分開記錄
        print(table0)
        print(table1)
        return max(table0[N-2], table0[N-3], table1[N-1], table1[N-2])
        # 答案可能是 (0 及 N-2) 或 (1 及 N-1)...
# 下面測資很好用
# [0,0,99,0,99]
# [1,2,3,4,5,1,2,3,4,5]
