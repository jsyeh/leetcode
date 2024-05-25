# LeetCode 140. Word Break II
# 字串 s 想要用 wordDict 字典來斷字，要全部順利「斷字」到最後
# 希望合理的斷字，看起來用「函式呼叫函式」可以解決。
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        N = len(s)  # 
        ans, now = [], []  # ans 最後放全部的答案，now 有斷字的過程
        def helper(i):
            if i==N:  # 順利走到最後，可記錄這組答案 now
                now2 = ' '.join(now) # 將現在的答案「轉成字串」
                ans.append(now2)  # 再記下這組答案
                return
            for word in wordDict:
                if i+len(word)<=N and s[i:i+len(word)]==word:
                    now.append(word)  # 可用這個word
                    helper(i+len(word))  # 繼續深究/往右斷字
                    now.pop()  # 退還回去，不要用這個 word
        helper(0)
        return ans
