# 題目保證有1個數 > 25%
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        N = len(arr)
        print(N)
        count = 1 # 第1個數出現，開始逐項比
        for i in range(N-1):
            if arr[i]==arr[i+1]:
                count += 1
            else:
                if count>N*0.25: # 如果總數>25%
                    return arr[i] # 就是答案
                count = 1
        # 如果離開迴圈時卻還沒回傳，表示最後1個數字是答案
        return arr[-1]
# case 24/25: [1,1,1,1,1,1,2,3,4,5,6,7,8,9,10,11,12,12,12,12]
