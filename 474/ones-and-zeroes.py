# LeetCode 474. Ones and Zeroes
# strs 陣列裡，有一堆「有0、有1」的字串，挑些字串「最多m個0、n個1」有幾種挑法？
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        counter = [Counter(s) for s in strs]  # 先統計好全部的數量
        @cache  # 想用「函式呼叫函式」來解
        def helper(i, m, n):  # 考慮要不要挑選 strs[i]
            if m<0 or n<0: return -inf  # 用盡了，不行！用「負無限大」這這條分支「不要拿來用
            if i >= len(strs): return 0  # 順利走到最後，恭喜！可開始「慢慢回推累積」了
            ans1 = helper(i+1, m-counter[i]['0'], n-counter[i]['1']) # 挑選 strs[i]
            ans2 = helper(i+1, m, n)  # 不挑選 sets[i]，後面繼續考慮「函式呼叫函式」
            return max(ans1+1, ans2)  # ans1 有挑選strs[i]，要+1
        ans = helper(0, m, n)  # 從 strs[0] 開始考慮，「函式呼叫函式」有幾種可能
        return ans
