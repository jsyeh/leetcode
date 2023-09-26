# 本來看不懂題目、不知道為什麼 cbacdcbc 會得到 acdb
# 後來看懂：刪掉重覆的字母，只留下單獨的字母，而且讓字母「照原有的順序」
# cbacdcbc
# --acd-b- 了解。接下來要怎麼解它呢？
# 我參考了 Editorial 的 Approach 2: Greedy - Solving with Stack 的投影片
# 使用了類似的作法來實作
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        ans = []
        last = {} # 這裡會記錄「某字母最後出現的位置」
        for i in range(len(s)):
            last[s[i]] = i # 這樣重覆記錄, 就會記下最後出現的index

        used = set() # 使用 set 的原因, 是希望 if c not in used 可以做得更有效率
        for i in range(len(s)):
            c = s[i]
            if c not in used: # 還沒用過, 就可以試看看
                while len(ans)>0 and ans[-1]>c and last[ans[-1]]>i:
                    # 前一個字母(後面)還會出現,且它比較大 (c比較小)
                    used.remove(ans[-1]) # 便可以取代它,所以先移除它
                    ans.pop() # 先移除它
                used.add(c) # 把c加進去
                ans.append(c) # 把c加進去

        return ('').join(ans) # 
