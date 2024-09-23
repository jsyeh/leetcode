# LeetCode 2707. Extra Characters in a String
# 字串 s 及字典 dictionary，s裡有些字母「沒在」字典裡，到底有幾個？
class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        d = set(dictionary)  # 先把所有的字，加到字典w裡
        N = len(s)  # N 是 ask()函式的「終止條件」
        @cache  # 使用 top-down dynamic programming 來查資料
        def ask(i: int) -> int:  # 利用函式呼叫函式，往右試「每種可能」
            if i==N: return 0 # 最後一格之後，N...N 這段字串裡，只剩0個字母
            # ans 對應「沒辦法被拆解成功的字母」有幾個
            ans = 1 + ask(i+1) # 先假裝這層放棄1個字，問i+1...N 的答案，+1後，當基礎答案
            # 接下來逐個位置拆解 i...N-1 這段字串，能順利被拆解嗎？
            for k in range(i, N):  # 利用函式呼叫函式，往右試「每種可能」
                if s[i:k+1] in d:  # 如果 i...k 能被順利拆解，那答案可以再小一點
                    ans = min(ans, ask(k+1))  # 利用函式呼叫函式，往右試「每種可能」
            return ans  # 最後、最小的 min extra character

        return ask(0)  # s 的最前面開始拆解，「問問看」答案算出來
