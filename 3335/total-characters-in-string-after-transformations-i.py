# LeetCode 3335. Total Characters in String After Transformations I
# transform 1 次，字母會往右1格（a變b,b變c..,z變ab) 問 t 次後，變幾個字母
class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        MOD = 10**9+7  # 因為 t 很大，要取餘數
        @cache  # 利用「函式呼叫函式」解這個題目
        def helper(t):  # 減參數，變成「字母'a'」經 t 次轉換後，變成幾個字母
            if t < 26: return 1  # 字母 'a' 在 25 次之內，都還是1個字母
            return (helper(t-26) + helper(t-26+1)) % MOD
            # 用掉26次，變字母'a'  + 用到 26次，變字母'b'再抬升1次，變字母'a'
        ans = 0
        for c in s:
            diff = ord(c) - ord('a')  # 要抬升 diff 次，會變字母'a'
            ans += helper(t+diff)  # 字母'a' 轉換 t+diff 次
        return ans % MOD
