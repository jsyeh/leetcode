class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        N = len(s)
        d = set()
        for w in dictionary:
            d.add(w) # 把所有的字，加到字典w裡

        @cache
        def ask(i: int) -> int:
            if i==N: return 0 # 最後一格之後，代表0個字

            ans = 1 + ask(i+1) # 先假裝這層放棄1個字，再問
            for k in range(i, N):
                if s[i:k+1] in d:
                    ans = min(ans, ask(k+1))
            return ans
        
        return ask(0)
        
