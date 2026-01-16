# LeetCode 216. Combination Sum III
# 將 1 到 9 的數，挑 k 個數（都只用1次）加起來是n
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        def helper(i, nowSum, nowList):  # 考慮「現在要不要使用 i 這個數」現在累積now
            if nowSum > n: return  # 提早超過、提早結束
            if len(nowList)>k: return  # 個數超過、提早結束
            if i==10:
                if nowSum==n and len(nowList)==k: ans.append(nowList)
                return
            helper(i+1, nowSum+i, nowList + [i])
            helper(i+1, nowSum, nowList)
        helper(1, 0, [])
        return ans
