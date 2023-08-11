# 利用 + 或 - 能湊出 target sum 的方法 ways[i][t]
# 不過target: -1000...+1000 有負數，所以陣列的範圍需要微調，以便都在範圍內
# 剛好 Python可以接受 index 為負，可善用這個特質
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        N = len(nums)
        total = sum(nums) # 這麼好，剛好sum()可以用
        # 有正有負的話，全負的數是 -total，所以陣列要 ways[N][total+target]
        if target>total or target<-total: # 運氣好 total必為正，可這樣寫
            return 0 # 超過能力範圍，做不到
        ways = [[0]*(total*2+1) for _ in range(N)]
        T21 = total*2+1
        # ways[i][t] 表示使用第 i 個數字，能湊到t的方法
        # t的範圍部分 -total ... 0 ... +total 總共有 total*2+1 個數
        # 剛好 Python可以接受 index 為負，可善用這個特質
        # 註：Python 的陣列有特異功能，可以有 [-total] 之類負數，剛好可用

        ways[0][+nums[0]] = 1
        ways[0][-nums[0]] += 1 # 原本是 = 1 
        # 但怕 nums[0] 是0的話，+0 -0 都要算1次，就改用 += 1

        for i in range(1, N): # 使用第i個數
            for t in range(total*2+1): # 每個格子都做檢查
                prev = ways[i-1][t] # 之前[t]有值
                if prev > 0: # 之前有在 [n] 放值，可做計算
                    ways[i][t-nums[i]] += prev # 放負號-nums[i]
                    ways[i][(t+nums[i])%T21] += prev #放正號+nums[i]
                    # %T21 即 %(total*2+1) 讓ways t+nums[i]不要超過範圍
        # print(ways)
        return ways[-1][target] # target是正是負，都可以
        # [-1] 就是 [N-1] 的意思,也就是最後的那個數
