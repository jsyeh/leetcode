# LeetCode 216. Combination Sum III
# 將 1 到 9 的數，挑 k 個數（都只用1次）加起來是n
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        # 不能真的用 itertools 的 combinations (但竟然可以通過，哈哈)
        a = range(1,10)
        ans = []
        for b in combinations(a, k):
            if sum(b)==n: ans.append(b)
        return ans
        
