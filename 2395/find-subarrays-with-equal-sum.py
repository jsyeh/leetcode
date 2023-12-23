# 想看看 nums 裡「連續的數」是否有「sum相同」的狀況
# 應可用 set()來做到，配合暴力巡頭尾 two pointers
# 但題目要求「長度剛好為2」的連續的數，更簡單
class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        sumSet = set()
        N = len(nums)
        # 這題不需用到 running sum, 因「長度剛好為2」的和
        # 直接算就好了
        for i in range(N-1):
            now = nums[i] + nums[i+1]
            if now in sumSet: # 有出現過，提早結束
                return True
            else: # 沒出現過
                sumSet.add(now) # 就記下來
        return False # 都沒提早結束，便是沒有

        '''
        # 以下是 running sum 但沒必要，因題目不是「任意長度」
        runSum = [0]*(N+1) # runSum[i+1] 對應 nums[0]..nums[i]
        for i in range(N): # 建立 running sum
            runSum[i+1] = runSum[i] + nums[i]
        print(runSum)
        for i in range(N):
            for j in range(i+2,N+1): # 右不包含
                now = runSum[j] - runSum[i]
                if now in sumSet: 
                    print(i,j,now)
                    print(sumSet)
                    return True # 有，提早結束
                else: 
                    sumSet.add(now)
        return False # 都沒提早結束，便是沒有
        '''
