# LeetCode 1304. Find N Unique Integers Sum up to Zero
# 隨便找到 n 個(不同的)數字，讓它們加起來是 0
# 感覺有點太隨便了，好像隨便寫，答案就可以正確了
class Solution:
    def sumZero(self, n: int) -> List[int]:
        ans = [i for i in range(1,n)]  # 先做出 1...n-1 項
        ans.append(-sum(ans))  # 最後一項，用負的，剛好合起來就變成0了
        return ans
