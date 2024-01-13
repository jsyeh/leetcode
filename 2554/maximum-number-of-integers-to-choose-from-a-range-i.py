# banned 不能用，1...n 範圍內，有多少數「加起來」不超過 maxSum
# 可以用 greedy 法，從小到大，試試看「最多」能加幾個數
# 因 10^4 
class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned = set(banned) # 變成集合，會比較快
        now = 0 # 由小到大，現在加總的結果
        ans = 0 # 現在有幾個數字
        for i in range(1,n+1): # 從小到大，逐去測
            if i not in banned:
                now += i # 加上現在的數
                if now<=maxSum: ans += 1 # 沒超過的話，很好
                else: return ans # 超過的話，提早結束
        return ans
