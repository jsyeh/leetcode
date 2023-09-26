# 這題和 316. Remove Duplicate Letters 相同, 所以我寫完 316 後, 接著來寫這題
# 使用 stack 的方法來解
class Solution:
    def smallestSubsequence(self, s: str) -> str:
        ans = [] # stack 在這裡, 裡面存可能的答案。有更小的值時, 便更新

        last = {} # 字母最後出現的位置
        for i in range(len(s)):
            last[s[i]] = i # 記下字母s[i]出現的位置i, 持續更新, 便是最後出現的位置
        
        for i in range(len(s)):
            c = s[i]
            if c not in ans:
                while len(ans)>0 and ans[-1]>c and last[ans[-1]]>i:
                    # 如果 ans 夠大, 且 ans[-1]最後1個字母比c大, 且會再出現
                    # 那就犠牲掉 ans[-1]吧
                    ans.pop()
                    # 把能移掉的都移掉後
                ans.append(c) # 現在的c就是最適合的了
        return "".join(ans) # 把 list 變成 string

        
