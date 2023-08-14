# 找 subarray 裡，有同樣數量的 0 and 1
# 想到一個方法，是將 0 當成-1， 1當成1，做running sum
# 用 hashmap 找sum[i]之前相同值 sum[k] 的位置， i-k即長度
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        N = len(nums)
        sum = [0]*(N+1) # 需要多個 sum[-1] 當 -1 格
        sum[-1] = 0 # 這樣比較好減

        ans = 0
        table = {} # hashmap
        table[0] = -1 # 因 sum[-1] = 0
        for i in range(N):
            sum[i] = sum[i-1] + nums[i] # 可把 1 加入
            if nums[i]==0: sum[i] -= 1 # 把0當 -1 加入

            if sum[i] in table: 
            # 若此數出現過，相減為0，有相同的-1,+1，是答案
                k = table[sum[i]] # 取出互補數
                if i - k > ans: ans = i - k # 更大長度
            if sum[i] not in table: # 若此數值未加入
                table[sum[i]] = i # 記錄它位置供之後比對
        return ans
# case 320/564: [0,0,1,0,0,0,1,1]
