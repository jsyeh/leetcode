# 剛完成 494. Target Sum 可以看「有正有負」的nums可以湊到哪些數
# 剛好這題能用這個技巧來完成，讓 target 為0即可
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        N = len(nums)
        total = sum(nums)
        T21 = total*2+1
        table = [[0]*T21 for _ in range(N)]
        # table[i][t] 表示 使用 nums[i] 能湊到 t 的可能性

        table[0][nums[0]]=1
        table[0][-nums[0]]=1 # 因 nums[i]>=1 所以不會是0,不需要 +=1

        for i in range(1,N): # 現在要試 nums[i]
            for t in range(T21): # 全部的格子都巡一次
                if table[i-1][t] > 0: # 有值，便有加減的可能性
                    table[i][t-nums[i]] += table[i-1][t]
                    table[i][(t+nums[i])%T21] += table[i-1][t]
        return table[-1][0]>0 # 如果利用+號 -號 分成2組，加總為0的可能性
        # 剛好有解
