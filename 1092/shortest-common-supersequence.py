# LeetCode 1092. Shortest Common Supersequence 
# 把 str1 和 str2 重覆（可疊在一起）後，做出「最短」的字串 ans
# 反過來說，str1 和 str2 都是 ans 的 subsequence (可「跳過」一些中間字母）
# Hint 1 找 str1[i:] 和 str2[j:] 的 LCS （可用DP找出來）
# Hint 2 LCS 是 ans 可共用部分，不能共用的部分，要再插入 ans 裡
# 題目看似簡單，但是這幾天 DP 系列「最後大魔王」。我一開始先用「函式呼叫函式」解出 LCS，很開心。
# 但接下來，要怎麼延伸呢？我想到「改裝LCS函式」，讓它「回傳2個字串」，包含 LCS 及題目講的 SCS
# 我完成之後，很得意！結果程式送出時，在第 46 筆測試資料發生「Memeory耗盡」的問題。
# 後來又做了幾次改造，還是「Memory耗盡」。最後去看「很多人的解答」都用 while 迴圈「湊答案」
# 先把 LCS 準備好，再用 while 迴圈，把「缺漏」的字母補起來。就這樣完成了。祝大家 LeetCode 快樂！
class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        @cache
        def LCS(i, j):
            if i==len(str1) or j==len(str2):
                return ''
            if str1[i]==str2[j]:
                return str1[i] + LCS(i+1, j+1)
            temp1 = LCS(i+1, j)
            temp2 = LCS(i, j+1)
            if len(temp1)>len(temp2): return temp1
            else: return temp2
        i, j = 0, 0
        ans = []
        for c in LCS(0,0):  # 找到共通的部分，接下來，用 while迴圈，把不同的部分「塞進去」
            while i<len(str1) and str1[i]!=c:
                ans.append(str1[i])
                i+=1
            while j<len(str2) and str2[j]!=c:
                ans.append(str2[j])
                j+=1
            i, j = i+1, j+1
            ans.append(c)
        ans.append(str1[i:])
        ans.append(str2[j:])
        return ''.join(ans)


        # 以下寫法，在「大測資」時，會「Memory耗盡」
        @cache
        def helper(i, j):  # 對應反過來的 LCS
            if i==len(str1):
                return str2[j:]
            elif j==len(str2):
                return str1[i:]
            
            if str1[i]==str2[j]:
                return str1[i] + helper(i+1, j+1)
            temp1 = str1[i] + helper(i+1, j)
            temp2 = str2[j] + helper(i, j+1)
            if len(temp1) < len(temp2):
                return temp1
            else:
                return temp2
        return helper(0, 0)
        
        # 以下寫法，在「大測資」時，會「Memory耗盡」
        def LCS(i, j):  # 找出兩字串的共同部分
            # 左邊是super，右邊是sub
            if i==len(str1):
                return str2[j:], ''
            if j==len(str2):
                return str1[i:], ''
            if str1[i]==str2[j]:
                S1, S2 = LCS(i+1,i+1)
                return str1[i] + S1, str1[i] + S2

            a1, a2 = LCS(i+1,j)
            b1, b2 = LCS(i,j+1)
            if len(a2)>len(b2):
                return str2[j] + a1, a2
            if len(a2)<len(b2):
                return str1[i] + b1, b2
            elif len(a1)<len(b1):
                return str2[j] + a1, a2
            else:
                return str1[i] + b1, b2

        s1, s2 = LCS(0, 0)
        return s1  # 把 super 回傳
