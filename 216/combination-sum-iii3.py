# LeetCode 216. Combination Sum III
# 將 1 到 9 的數，挑 k 個數（都只用1次）加起來是n
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        now = []
        def helper(i, k, n):  # 要挑 k 個數，加起來是 n，目前考慮 i
            if i==10: 
                if k==0 and n==0: ans.append(list(now))
                return
            now.append(i)
            helper(i+1,k-1,n-i)
            now.pop()
            helper(i+1,k,n)
        helper(1,k,n)
        return ans
