# 這題可看成是 LeetCode 560. Subarray Sum Equals K 進階版
# 重點在(1) running sum, (2) Hash Map, (3) 兩個方向都做一次
class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        M, N = len(matrix), len(matrix[0])
        for i in range(M): # 左手i
            for j in range(1,N): # 右手j # 避開最左邊項
                matrix[i][j] += matrix[i][j-1]
            matrix[i].insert(0, 0) # 奇怪技巧，最左邊多1項0
            # 要簡化減法 matrix[i][j2] - matrix[i][j1] 
        ans = 0 # 收集答案（有幾組）
        for j1 in range(N+1): # 因為多了1項 j1在偏左
            for j2 in range(j1+1, N+1): # 右手的j2
                # j1...j2 決定左右範圍 j1不包含，j2包含
                counter = Counter() # Hash Map 計數字
                counter[0] = 1 # 最前面的
                nowSum = 0 # 上到下的 running sum
                # i 會往下展開
                for i in range(M):
                    # nowSum 是上到下的 running sun (在j1..j2的範圍)
                    nowSum += matrix[i][j2]-matrix[i][j1]
                    if counter[nowSum-target]: # 幸運出現過
                        ans += counter[nowSum-target] # 收集答案
                    counter[nowSum] += 1 # 再入 hash map
        return ans
# 遇到Hard題目 1074. Number of Submatrices That Sum to Target
# 它的簡化版，就是這題 560. Subarray Sum Equals K
# 所以重寫這題看看，重點(1) running sum 可簡化加總的迴圈
# (2) Hash Map 可簡化找到「是否有重覆出現需要的數字」
''' # 以下是 LeetCode 560. Subarray Sum Equals K
# 也就是本題的 1D 的版本，附在後面參考
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # 先做 running sum 簡化加總的問題
        N = len(nums)
        for i in range(1,N): # 因為nums[0]不用加，從1開始
            nums[i] += nums[i-1] # 變成 running sum
        # 到這裡為址 nums[i] 便成為 running sum 了
        # 也就是原本 nums[i]+...+nums[j] 會變成 nums[j]-nums[i-1]
        counter = Counter() # 可計數的 hash map
        counter[0] = 1 # 最左邊會 running sum 0出現1次
        ans = 0 # 數數看有多少可能
        for i in range(N):
            # nums[i] - prev 會得到 k 嗎？
            prev = nums[i] - k # 想問之前有沒有出現 prev
            if counter[prev]>0: # 有幸出現過，可加出k
                ans += counter[prev] # 就增加對應的可能
            counter[nums[i]] += 1 # 多發明一個數字哦
        return ans
'''
