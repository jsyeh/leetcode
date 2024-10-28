# LeetCode 1228. Missing Number In Arithmetic Progression
# 找到「等差級數」中，缺的那個數
class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        diff1, diff2 = arr[1]-arr[0], arr[2]-arr[1]
        if diff1<0: diff = max(diff1, diff2)
        else: diff = min(diff1, diff2)
        # 找到等差級數的 diff 值了
        if diff==0: return arr[0] # 如果差值是0，那漏的數也是同個數
        
        for i in range(len(arr)-1):  # 兩兩比較
            if arr[i+1]-arr[i] != diff:
                return arr[i] + diff;
