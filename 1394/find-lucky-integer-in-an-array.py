# lucky integer: 陣列中出現的次數，剛好是自己本身
# 找最大的 lucky integer
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        counter = Counter(arr)
        ans = -1 # 預設的答案
        for n in counter: # 依照統計結果，逐一比較
            if n==counter[n]: ans = max(ans, n) # lucky!
        return ans
